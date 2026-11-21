"""Contrato del puerto RepositorioClinico (memoria y SQLite) y comportamiento propio de SQLite."""
import os
import sqlite3
import tempfile
from dataclasses import replace
from datetime import date
from decimal import Decimal

import pytest

from src.dominio.entidades import Consulta
from src.infraestructura.repositorios import (
    ErrorPersistencia, RepositorioClinicoEnMemoria, RepositorioClinicoSQLite)

IMPLEMENTACIONES = [pytest.param(RepositorioClinicoEnMemoria, id="memoria"),
                    pytest.param(RepositorioClinicoSQLite, id="sqlite")]


def consulta(historia_id=1, **cambios):
    base = Consulta(id=0, historia_id=historia_id, veterinario_id=1, fecha=date(2026, 11, 2),
                    peso=Decimal("5.20"), sintomas="Fiebre", diagnostico="Control", observaciones="")
    return replace(base, **cambios)


def peso_vigente(repo, mascota_id=1):
    return repo.obtener_contexto(mascota_id)[0].peso_actual


@pytest.mark.parametrize("fabrica", IMPLEMENTACIONES)
class TestContrato:
    def test_contexto_de_mascota_existente(self, fabrica):
        """CP-32."""
        mascota, historia = fabrica().obtener_contexto(1)
        assert (mascota.nombre, mascota.especie, mascota.peso_actual) == ("Luna", "Perro", Decimal("6.8"))
        assert historia.mascota_id == mascota.id

    def test_contexto_de_mascota_inexistente(self, fabrica):
        """CP-33."""
        assert fabrica().obtener_contexto(999) is None

    def test_historia_vacia_al_inicio(self, fabrica):
        """CP-34."""
        assert fabrica().listar_consultas(1) == []

    def test_asigna_ids_consecutivos(self, fabrica):
        """CP-35."""
        repo = fabrica()
        primera = repo.guardar_consulta(consulta())
        segunda = repo.guardar_consulta(consulta())
        assert (primera.id, segunda.id) == (1, 2)

    def test_conserva_tipos_y_valores(self, fabrica):
        """CP-36: date y Decimal vuelven exactos (peso 0.10 no se vuelve float)."""
        repo = fabrica()
        guardada = repo.guardar_consulta(consulta(peso=Decimal("0.10"), observaciones="ok"))
        leida = repo.listar_consultas(1)[0]
        assert leida == guardada
        assert isinstance(leida.fecha, date) and isinstance(leida.peso, Decimal)
        assert str(leida.peso) == "0.10"

    def test_separa_consultas_por_historia(self, fabrica):
        """CP-37."""
        repo = fabrica()
        repo.guardar_consulta(consulta(historia_id=1))
        repo.guardar_consulta(consulta(historia_id=2))
        assert [c.historia_id for c in repo.listar_consultas(1)] == [1]
        assert [c.historia_id for c in repo.listar_consultas(2)] == [2]

    def test_lista_de_la_mas_reciente_a_la_mas_antigua(self, fabrica):
        """CP-38: orden por fecha descendente; a igual fecha, la última guardada primero."""
        repo = fabrica()
        repo.guardar_consulta(consulta(sintomas="a", fecha=date(2026, 11, 5)))
        repo.guardar_consulta(consulta(sintomas="b", fecha=date(2026, 11, 1)))
        repo.guardar_consulta(consulta(sintomas="c", fecha=date(2026, 11, 5)))
        assert [c.sintomas for c in repo.listar_consultas(1)] == ["c", "a", "b"]

    def test_la_consulta_mas_reciente_actualiza_el_peso_vigente(self, fabrica):
        """CP-39 (CU-01 paso 6): Luna pasa de 6.8 a 5.84 kg."""
        repo = fabrica()
        repo.guardar_consulta(consulta(fecha=date(2026, 11, 21), peso=Decimal("5.84")))
        assert peso_vigente(repo) == Decimal("5.84")
        assert peso_vigente(repo, 2) == Decimal("4.1")   # la otra mascota no cambia

    def test_una_consulta_mas_antigua_no_pisa_el_peso_vigente(self, fabrica):
        """CP-40: cargar una consulta atrasada conserva el peso de la más nueva."""
        repo = fabrica()
        repo.guardar_consulta(consulta(fecha=date(2026, 11, 21), peso=Decimal("5.84")))
        repo.guardar_consulta(consulta(fecha=date(2026, 10, 1), peso=Decimal("7.00")))
        assert peso_vigente(repo) == Decimal("5.84")

    def test_misma_fecha_gana_la_ultima_guardada(self, fabrica):
        """CP-41: a igual fecha no hay consulta posterior, así que se actualiza."""
        repo = fabrica()
        repo.guardar_consulta(consulta(fecha=date(2026, 11, 21), peso=Decimal("5.84")))
        repo.guardar_consulta(consulta(fecha=date(2026, 11, 21), peso=Decimal("5.90")))
        assert peso_vigente(repo) == Decimal("5.90")

    def test_historia_inexistente_se_rechaza_sin_guardar(self, fabrica):
        """CP-42."""
        repo = fabrica()
        with pytest.raises(ValueError):
            repo.guardar_consulta(consulta(historia_id=999))
        assert repo.listar_consultas(1) == [] and peso_vigente(repo) == Decimal("6.8")


class TestSQLite:
    def test_carga_los_datos_iniciales(self):
        """CP-43: dos mascotas con una historia cada una."""
        repo = RepositorioClinicoSQLite()
        assert repo.obtener_contexto(2)[0].nombre == "Toby"
        assert repo.obtener_contexto(2)[1].id == 2

    def test_sin_sembrar_la_base_queda_vacia(self):
        """CP-44."""
        assert RepositorioClinicoSQLite(sembrar_demo=False).obtener_contexto(1) is None

    def test_los_datos_persisten_al_reabrir_y_la_siembra_no_los_pisa(self):
        """CP-45: la consulta y el peso vigente sobreviven a un reinicio (no vuelve a 6.8)."""
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "datos", "vet.db")      # la carpeta se crea sola
            repo = RepositorioClinicoSQLite(ruta)
            repo.guardar_consulta(consulta(sintomas="persistente", peso=Decimal("5.84")))
            repo.cerrar()
            reabierto = RepositorioClinicoSQLite(ruta)
            assert [c.sintomas for c in reabierto.listar_consultas(1)] == ["persistente"]
            assert peso_vigente(reabierto) == Decimal("5.84")
            assert reabierto.guardar_consulta(consulta()).id == 2
            reabierto.cerrar()

    def test_falla_al_guardar_no_deja_datos_parciales(self):
        """CP-46 (EC-03): veterinario inexistente (clave foránea): rollback; ni consulta ni peso cambian."""
        repo = RepositorioClinicoSQLite()
        with pytest.raises(ErrorPersistencia):
            repo.guardar_consulta(consulta(veterinario_id=999, peso=Decimal("9.99")))
        assert repo.listar_consultas(1) == []
        assert peso_vigente(repo) == Decimal("6.8")
        assert repo.guardar_consulta(consulta()).id == 1     # sigue operativa tras la falla

    def test_las_restricciones_de_la_base_son_la_ultima_defensa(self):
        """CP-47: peso 0 o síntomas vacíos violan un CHECK y se informan, sin ignorarse en silencio."""
        repo = RepositorioClinicoSQLite()
        for malo in (consulta(peso=Decimal("0")), consulta(sintomas=""), consulta(sintomas=None)):
            with pytest.raises(ErrorPersistencia):
                repo.guardar_consulta(malo)
        assert repo.listar_consultas(1) == []

    def test_al_reabrir_una_base_existente_siguen_activas_las_claves_foraneas(self):
        """CP-48: el PRAGMA se aplica en cada conexión."""
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "vet.db")
            RepositorioClinicoSQLite(ruta).cerrar()
            reabierto = RepositorioClinicoSQLite(ruta)
            with pytest.raises(ErrorPersistencia):
                reabierto.guardar_consulta(consulta(veterinario_id=999))
            reabierto.cerrar()

    def test_una_mascota_no_puede_tener_dos_historias(self):
        """CP-49: la relación 1 a 1 del dominio se refleja con UNIQUE."""
        repo = RepositorioClinicoSQLite()
        with pytest.raises(sqlite3.IntegrityError):
            repo._con.execute("INSERT INTO historias (id, mascota_id) VALUES (99, 1)")

    def test_errores_de_la_base_se_traducen(self):
        """CP-50: una base cerrada produce ErrorPersistencia en las tres operaciones."""
        repo = RepositorioClinicoSQLite()
        repo.cerrar()
        for operacion in (lambda: repo.obtener_contexto(1),
                          lambda: repo.listar_consultas(1),
                          lambda: repo.guardar_consulta(consulta())):
            with pytest.raises(ErrorPersistencia):
                operacion()
