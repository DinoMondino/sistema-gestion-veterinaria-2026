"""HU-01: pruebas unitarias del validador, servicio y repositorio (sin interfaz)."""
from datetime import date, timedelta
from decimal import Decimal

import pytest

from src.aplicacion.servicio_registro import ServicioRegistroClinico
from src.aplicacion.validacion import ValidacionRegistrosClinicos
from src.infraestructura.repositorios import RepositorioClinicoEnMemoria


def datos_validos():
    return {
        "fecha": date.today().isoformat(),
        "peso": "5.2",
        "sintomas": "Fiebre",
        "diagnostico": "Control clínico",
        "observaciones": "Sin novedades",
    }


@pytest.mark.parametrize("cambio,campo", [
    pytest.param({"fecha": ""}, "fecha", id="CP-01"),
    pytest.param({"fecha": "2026-02-31"}, "fecha", id="CP-02"),
    pytest.param({"fecha": (date.today() + timedelta(days=1)).isoformat()}, "fecha", id="CP-03"),
    pytest.param({"peso": "-5"}, "peso", id="CP-04"),
    pytest.param({"peso": "0"}, "peso", id="CP-05"),
    pytest.param({"peso": "texto"}, "peso", id="CP-06"),
    pytest.param({"peso": "NaN"}, "peso", id="CP-07"),
    pytest.param({"sintomas": "   "}, "sintomas", id="CP-08"),
    pytest.param({"diagnostico": ""}, "diagnostico", id="CP-09"),
])
def test_rechaza_campos_invalidos(cambio, campo):
    datos = datos_validos()
    datos.update(cambio)
    _, errores = ValidacionRegistrosClinicos().validar(datos)
    assert campo in errores
    assert errores[campo]  # mensaje específico, no vacío


def test_rechaza_varios_campos_en_un_solo_intento():
    datos = datos_validos()
    datos.update(fecha="", peso="-5")
    _, errores = ValidacionRegistrosClinicos().validar(datos)
    assert set(errores) == {"fecha", "peso"}


def test_admite_valores_limite_validos_y_normaliza():
    datos = datos_validos()
    datos.update(peso="0,01", sintomas="  Fiebre  ", observaciones="  Control  ")
    normalizados, errores = ValidacionRegistrosClinicos().validar(datos)
    assert errores == {}
    assert normalizados["peso"] == Decimal("0.01")
    assert normalizados["sintomas"] == "Fiebre"
    assert normalizados["observaciones"] == "Control"
    assert normalizados["fecha"] == date.today()


def test_observaciones_opcionales():
    datos = datos_validos()
    datos.pop("observaciones")
    normalizados, errores = ValidacionRegistrosClinicos().validar(datos)
    assert errores == {}
    assert normalizados["observaciones"] == ""


def test_servicio_rechaza_sin_guardar():
    repo = RepositorioClinicoEnMemoria()
    servicio = ServicioRegistroClinico(repo, ValidacionRegistrosClinicos())
    datos = datos_validos()
    datos.update(peso="-5", fecha="")
    resultado = servicio.registrar(1, datos)
    assert resultado.estado == "invalido"
    assert set(resultado.errores) == {"fecha", "peso"}
    assert resultado.consulta is None
    assert repo.listar_consultas(1) == []
    assert datos["sintomas"] == "Fiebre"  # el diccionario de entrada no se altera


def test_servicio_guarda_consulta_valida():
    repo = RepositorioClinicoEnMemoria()
    servicio = ServicioRegistroClinico(repo, ValidacionRegistrosClinicos())
    resultado = servicio.registrar(1, datos_validos())
    assert resultado.estado == "creado"
    assert resultado.errores == {}
    assert resultado.consulta.id == 1
    assert repo.listar_consultas(1) == [resultado.consulta]


def test_servicio_mascota_inexistente():
    repo = RepositorioClinicoEnMemoria()
    resultado = ServicioRegistroClinico(repo, ValidacionRegistrosClinicos()).registrar(999, datos_validos())
    assert resultado.estado == "no_encontrado"
    assert repo.listar_consultas(1) == []


def test_repositorio_mascota_y_historia_relacionadas():
    repo = RepositorioClinicoEnMemoria()
    mascota, historia = repo.obtener_contexto(1)
    assert historia.mascota_id == mascota.id
    assert repo.obtener_contexto(999) is None


def test_repositorio_consultas_separadas_por_historia():
    repo = RepositorioClinicoEnMemoria()
    servicio = ServicioRegistroClinico(repo, ValidacionRegistrosClinicos())
    servicio.registrar(1, datos_validos())
    servicio.registrar(2, datos_validos())
    assert len(repo.listar_consultas(1)) == 1
    assert len(repo.listar_consultas(2)) == 1
    assert repo.listar_consultas(1)[0].id != repo.listar_consultas(2)[0].id
