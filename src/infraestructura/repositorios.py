"""Puerto de persistencia y sus implementaciones: memoria y SQLite (TP4 Parte B).

Contrato de guardar_consulta: en UNA transacción almacena la consulta y, si es
la más reciente de la historia (por fecha), actualiza el peso vigente de la
mascota (CU-01, paso 6). Si algo falla no queda ninguno de los dos cambios.
"""
import sqlite3
from abc import ABC, abstractmethod
from dataclasses import replace
from datetime import date
from decimal import Decimal
from pathlib import Path
from threading import RLock

from src.dominio.entidades import Consulta, HistoriaClinica, Mascota, Veterinario


class ErrorPersistencia(Exception):
    """La base no pudo completar la operación; no quedó ningún dato parcial."""


class RepositorioClinico(ABC):
    @abstractmethod
    def obtener_contexto(self, mascota_id: int):
        """Devuelve (mascota, historia) o None."""

    @abstractmethod
    def guardar_consulta(self, consulta: Consulta) -> Consulta:
        """Almacena una consulta válida, actualiza el peso vigente si
        corresponde y devuelve la consulta con ID asignado.
        Lanza ValueError si la historia clínica no existe y
        ErrorPersistencia si la base falla."""

    @abstractmethod
    def listar_consultas(self, historia_id: int) -> list[Consulta]:
        """Lista consultas, de la más reciente a la más antigua."""


class RepositorioClinicoEnMemoria(RepositorioClinico):
    def __init__(self):
        self._lock = RLock()
        self.mascotas = {1: Mascota(1, "Luna", "Perro", Decimal("6.8")),
                         2: Mascota(2, "Toby", "Gato", Decimal("4.1"))}
        self.historias = {1: HistoriaClinica(1, 1), 2: HistoriaClinica(2, 2)}
        self.veterinario_demo = Veterinario(1, "Dra. Ana Ríos")
        self._consultas: list[Consulta] = []
        self._siguiente_id = 1

    def obtener_contexto(self, mascota_id: int):
        mascota = self.mascotas.get(mascota_id)
        historia = self.historias.get(mascota_id)
        return (mascota, historia) if mascota and historia else None

    def guardar_consulta(self, consulta: Consulta) -> Consulta:
        with self._lock:
            historia = next((h for h in self.historias.values()
                             if h.id == consulta.historia_id), None)
            if historia is None:
                raise ValueError("Historia clínica inexistente.")
            hay_posterior = any(c.historia_id == historia.id and c.fecha > consulta.fecha
                                for c in self._consultas)
            creada = replace(consulta, id=self._siguiente_id)
            self._siguiente_id += 1
            self._consultas.append(creada)
            if not hay_posterior:
                mascota = self.mascotas[historia.mascota_id]
                self.mascotas[mascota.id] = replace(mascota, peso_actual=creada.peso)
            return creada

    def listar_consultas(self, historia_id: int) -> list[Consulta]:
        with self._lock:
            propias = [c for c in self._consultas if c.historia_id == historia_id]
        return sorted(propias, key=lambda c: (c.fecha, c.id), reverse=True)


_ESQUEMA = """
CREATE TABLE IF NOT EXISTS veterinarios (
    id     INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS mascotas (
    id          INTEGER PRIMARY KEY,
    nombre      TEXT NOT NULL,
    especie     TEXT NOT NULL,
    peso_actual TEXT NOT NULL CHECK (CAST(peso_actual AS REAL) > 0)
);
CREATE TABLE IF NOT EXISTS historias (
    id         INTEGER PRIMARY KEY,
    mascota_id INTEGER NOT NULL UNIQUE REFERENCES mascotas(id)
);
CREATE TABLE IF NOT EXISTS consultas (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    historia_id    INTEGER NOT NULL REFERENCES historias(id),
    veterinario_id INTEGER NOT NULL REFERENCES veterinarios(id),
    fecha          TEXT NOT NULL,
    peso           TEXT NOT NULL CHECK (CAST(peso AS REAL) > 0),
    sintomas       TEXT NOT NULL CHECK (length(sintomas) > 0),
    diagnostico    TEXT NOT NULL CHECK (length(diagnostico) > 0),
    observaciones  TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_consultas_historia
    ON consultas (historia_id, fecha DESC, id DESC);
"""


class RepositorioClinicoSQLite(RepositorioClinico):
    """Persistencia en SQLite. Pesos como TEXT para conservar la exactitud de Decimal.

    Toda falla de la base (sqlite3.Error) se informa como ErrorPersistencia.
    """

    def __init__(self, ruta=":memory:", sembrar_demo: bool = True):
        if str(ruta) != ":memory:":
            Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        self._lock = RLock()
        # Flask atiende en hilos distintos: una conexión compartida, serializada por el lock.
        self._con = sqlite3.connect(str(ruta), check_same_thread=False)
        self._con.row_factory = sqlite3.Row
        self._con.execute("PRAGMA foreign_keys = ON")
        with self._lock, self._con:
            self._con.executescript(_ESQUEMA)
        if sembrar_demo:
            self._sembrar_demo()

    def _sembrar_demo(self):
        """Datos de demostración; idempotente (no pisa datos existentes)."""
        with self._lock, self._con:
            self._con.execute("INSERT OR IGNORE INTO veterinarios VALUES (1, 'Dra. Ana Ríos')")
            self._con.executemany(
                "INSERT OR IGNORE INTO mascotas VALUES (?, ?, ?, ?)",
                [(1, "Luna", "Perro", "6.8"), (2, "Toby", "Gato", "4.1")])
            self._con.executemany("INSERT OR IGNORE INTO historias VALUES (?, ?)",
                                  [(1, 1), (2, 2)])

    def cerrar(self):
        with self._lock:
            self._con.close()

    def obtener_contexto(self, mascota_id: int):
        try:
            with self._lock:
                m = self._con.execute("SELECT * FROM mascotas WHERE id = ?",
                                      (mascota_id,)).fetchone()
                h = self._con.execute("SELECT * FROM historias WHERE mascota_id = ?",
                                      (mascota_id,)).fetchone()
        except sqlite3.Error as error:
            raise ErrorPersistencia(str(error)) from error
        if m is None or h is None:
            return None
        return (Mascota(m["id"], m["nombre"], m["especie"], Decimal(m["peso_actual"])),
                HistoriaClinica(h["id"], h["mascota_id"]))

    def guardar_consulta(self, consulta: Consulta) -> Consulta:
        try:
            with self._lock, self._con:  # `with con` = commit, o rollback si hay excepción
                h = self._con.execute("SELECT mascota_id FROM historias WHERE id = ?",
                                      (consulta.historia_id,)).fetchone()
                if h is None:
                    raise ValueError("Historia clínica inexistente.")
                hay_posterior = self._con.execute(
                    "SELECT 1 FROM consultas WHERE historia_id = ? AND fecha > ? LIMIT 1",
                    (consulta.historia_id, consulta.fecha.isoformat())).fetchone()
                cursor = self._con.execute(
                    "INSERT INTO consultas (historia_id, veterinario_id, fecha, peso,"
                    " sintomas, diagnostico, observaciones) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (consulta.historia_id, consulta.veterinario_id,
                     consulta.fecha.isoformat(), str(consulta.peso), consulta.sintomas,
                     consulta.diagnostico, consulta.observaciones))
                if not hay_posterior:
                    self._con.execute("UPDATE mascotas SET peso_actual = ? WHERE id = ?",
                                      (str(consulta.peso), h["mascota_id"]))
                return replace(consulta, id=cursor.lastrowid)
        except sqlite3.Error as error:
            raise ErrorPersistencia(str(error)) from error

    def listar_consultas(self, historia_id: int) -> list[Consulta]:
        try:
            with self._lock:
                filas = self._con.execute(
                    "SELECT * FROM consultas WHERE historia_id = ?"
                    " ORDER BY fecha DESC, id DESC", (historia_id,)).fetchall()
        except sqlite3.Error as error:
            raise ErrorPersistencia(str(error)) from error
        return [Consulta(id=f["id"], historia_id=f["historia_id"],
                         veterinario_id=f["veterinario_id"],
                         fecha=date.fromisoformat(f["fecha"]),
                         peso=Decimal(f["peso"]), sintomas=f["sintomas"],
                         diagnostico=f["diagnostico"],
                         observaciones=f["observaciones"]) for f in filas]
