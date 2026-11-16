"""Puerto de persistencia e implementación en memoria (TP4 Parte B)."""
from abc import ABC, abstractmethod
from dataclasses import replace
from decimal import Decimal
from threading import Lock
from src.dominio.entidades import Consulta, HistoriaClinica, Mascota, Veterinario

class RepositorioClinico(ABC):
    @abstractmethod
    def obtener_contexto(self, mascota_id: int):
        """Devuelve (mascota, historia) o None."""

    @abstractmethod
    def guardar_consulta(self, consulta: Consulta) -> Consulta:
        """Almacena una consulta válida y devuelve su versión con ID asignado."""

    @abstractmethod
    def listar_consultas(self, historia_id: int) -> list[Consulta]:
        """Lista consultas almacenadas."""

class RepositorioClinicoEnMemoria(RepositorioClinico):
    def __init__(self):
        self._lock = Lock()
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
            creada = replace(consulta, id=self._siguiente_id)
            self._siguiente_id += 1
            self._consultas.append(creada)
            return creada

    def listar_consultas(self, historia_id: int) -> list[Consulta]:
        return [c for c in self._consultas if c.historia_id == historia_id]
