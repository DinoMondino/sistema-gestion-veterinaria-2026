"""RF-10 y RF-11 — ValidacionRegistrosClinicos. Caja negra (criterios de aceptación) y caja blanca (caminos)."""
from datetime import date, timedelta
from decimal import Decimal

import pytest

from datos_prueba import datos_validos
from src.aplicacion.validacion import ValidacionRegistrosClinicos

HOY = date.today()


def validar(**cambios):
    datos = datos_validos()
    datos.update(cambios)
    return ValidacionRegistrosClinicos().validar(datos)


@pytest.mark.parametrize("cambio,campo", [
    pytest.param({"fecha": ""}, "fecha", id="CP-01"),                                   # fecha en blanco
    pytest.param({"fecha": "2026-02-31"}, "fecha", id="CP-02"),                         # fecha inexistente
    pytest.param({"fecha": (HOY + timedelta(days=1)).isoformat()}, "fecha", id="CP-03"),  # límite: mañana
    pytest.param({"fecha": "15/01/2026"}, "fecha", id="CP-04"),                         # formato no ISO
    pytest.param({"peso": "-5"}, "peso", id="CP-05"),                                   # negativo
    pytest.param({"peso": "0"}, "peso", id="CP-06"),                                    # límite: cero
    pytest.param({"peso": "-0.01"}, "peso", id="CP-07"),                                # límite: apenas negativo
    pytest.param({"peso": "texto"}, "peso", id="CP-08"),                                # no numérico
    pytest.param({"peso": "NaN"}, "peso", id="CP-09"),
    pytest.param({"peso": "Infinity"}, "peso", id="CP-10"),
    pytest.param({"peso": ""}, "peso", id="CP-11"),
    pytest.param({"sintomas": "   "}, "sintomas", id="CP-12"),                          # solo espacios
    pytest.param({"diagnostico": ""}, "diagnostico", id="CP-13"),
])
def test_rechaza_un_campo_invalido_y_solo_ese(cambio, campo):
    _, errores = validar(**cambio)
    assert set(errores) == {campo}
    assert errores[campo]  # mensaje específico, no vacío (RF-11)


@pytest.mark.parametrize("datos", [
    pytest.param({}, id="CP-14a-claves-ausentes"),
    pytest.param({"fecha": None, "peso": None, "sintomas": None, "diagnostico": None}, id="CP-14b-valores-nulos"),
])
def test_campos_ausentes_se_informan_todos_juntos(datos):
    """CP-14 (EC-01, reducir sobrecarga): una sola pasada devuelve los cuatro errores."""
    _, errores = ValidacionRegistrosClinicos().validar(datos)
    assert set(errores) == {"fecha", "peso", "sintomas", "diagnostico"}


def test_rechaza_varios_campos_en_un_solo_intento():
    """CP-15: fecha en blanco y peso negativo (el criterio de aceptación de HU-01)."""
    _, errores = validar(fecha="", peso="-5")
    assert set(errores) == {"fecha", "peso"}


@pytest.mark.parametrize("cambio,campo,esperado", [
    pytest.param({"fecha": HOY.isoformat()}, "fecha", HOY, id="CP-16-fecha-hoy"),
    pytest.param({"fecha": (HOY - timedelta(days=1)).isoformat()}, "fecha", HOY - timedelta(days=1), id="CP-17-fecha-ayer"),
    pytest.param({"peso": "0,01"}, "peso", Decimal("0.01"), id="CP-18-peso-minimo-con-coma"),
    pytest.param({"peso": "5"}, "peso", Decimal("5"), id="CP-19-peso-entero"),
    pytest.param({"peso": " 5.2 "}, "peso", Decimal("5.2"), id="CP-20-peso-con-espacios"),
    pytest.param({"peso": 5.2}, "peso", Decimal("5.2"), id="CP-21-peso-numero-json"),
    pytest.param({"sintomas": "  Fiebre  "}, "sintomas", "Fiebre", id="CP-22-recorta-sintomas"),
    pytest.param({"observaciones": "  Control  "}, "observaciones", "Control", id="CP-23-recorta-observaciones"),
])
def test_acepta_valores_validos_y_los_normaliza(cambio, campo, esperado):
    normalizados, errores = validar(**cambio)
    assert errores == {}
    assert normalizados[campo] == esperado


def test_observaciones_son_opcionales():
    """CP-24."""
    datos = datos_validos()
    datos.pop("observaciones")
    normalizados, errores = ValidacionRegistrosClinicos().validar(datos)
    assert errores == {}
    assert normalizados["observaciones"] == ""


def test_con_errores_no_se_entregan_datos_invalidos_normalizados():
    """CP-25: el campo inválido no aparece entre los normalizados."""
    normalizados, errores = validar(peso="-5")
    assert "peso" in errores and "peso" not in normalizados
    assert "fecha" in normalizados  # los campos válidos sí
