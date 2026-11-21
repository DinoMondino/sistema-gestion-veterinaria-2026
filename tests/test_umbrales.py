"""Umbrales de integridad clínica de HU-01 (U-01 a U-09), CP-62 a CP-118.

Errores (bloquean, 422): U-01 a U-06.  Advertencias (piden confirmación, 409): U-07 a U-09.
"""
from datetime import date, timedelta
from decimal import Decimal

import pytest

from datos_prueba import RepositorioEspia, datos_validos, servicio_con
from src.aplicacion.validacion import ReferenciaPeso, ValidacionRegistrosClinicos
from src.dominio.entidades import Consulta
from src.infraestructura.repositorios import RepositorioClinicoSQLite

HOY = date.today()


# ------------------------------------------------------------------ errores (validar)
def validar(**cambios):
    datos = datos_validos()
    datos.update(cambios)
    return ValidacionRegistrosClinicos().validar(datos)


@pytest.mark.parametrize("cambio,campo", [
    pytest.param({"peso": "300.01"}, "peso", id="CP-62-U01-peso-apenas-sobre-el-maximo"),
    pytest.param({"peso": "1000"}, "peso", id="CP-63-U01-peso-muy-alto"),
    pytest.param({"peso": "5.123"}, "peso", id="CP-64-U02-tres-decimales"),
    pytest.param({"sintomas": "a"}, "sintomas", id="CP-65-U03-sintomas-un-caracter"),
    pytest.param({"sintomas": "Tos"}, "sintomas", id="CP-66-U03-sintomas-bajo-el-minimo"),
    pytest.param({"diagnostico": "ab"}, "diagnostico", id="CP-67-U03-diagnostico-bajo-el-minimo"),
    pytest.param({"sintomas": "aaaaaaa"}, "sintomas", id="CP-68-U04-caracter-repetido"),
    pytest.param({"sintomas": "12345 678"}, "sintomas", id="CP-69-U04-sin-letras"),
    pytest.param({"sintomas": "....."}, "sintomas", id="CP-70-U04-solo-signos"),
    pytest.param({"diagnostico": "ÁÁÁÁ"}, "diagnostico", id="CP-71-U04-tildes-no-engañan"),
    pytest.param({"diagnostico": "ASDF"}, "diagnostico", id="CP-72-U05-relleno-conocido"),
    pytest.param({"diagnostico": "a s d f"}, "diagnostico", id="CP-73-U05-relleno-con-espacios"),
    pytest.param({"sintomas": "Fiebre " * 150}, "sintomas", id="CP-74-U06-sintomas-demasiado-largos"),
    pytest.param({"diagnostico": "Otitis " * 60}, "diagnostico", id="CP-75-U06-diagnostico-demasiado-largo"),
    pytest.param({"observaciones": "Control " * 300}, "observaciones", id="CP-76-U06-observaciones-demasiado-largas"),
])
def test_umbral_de_error_rechaza_solo_ese_campo(cambio, campo):
    normalizados, errores = validar(**cambio)
    assert set(errores) == {campo}
    assert errores[campo]
    assert campo not in normalizados


@pytest.mark.parametrize("cambio,campo,esperado", [
    pytest.param({"peso": "300"}, "peso", Decimal("300"), id="CP-77-U01-peso-justo-en-el-maximo"),
    pytest.param({"peso": "5.25"}, "peso", Decimal("5.25"), id="CP-78-U02-dos-decimales"),
    pytest.param({"peso": "5.200"}, "peso", Decimal("5.200"), id="CP-79-U02-ceros-finales-no-cuentan"),
    pytest.param({"sintomas": "Cojea"}, "sintomas", "Cojea", id="CP-80-U03-sintomas-en-el-minimo"),
    pytest.param({"diagnostico": "IRA"}, "diagnostico", "IRA", id="CP-81-U03-diagnostico-en-el-minimo"),
    pytest.param({"observaciones": "Control " * 250}, "observaciones", ("Control " * 250).strip(),
                 id="CP-82-U06-observaciones-en-el-maximo"),
])
def test_valores_justo_en_el_limite_se_aceptan(cambio, campo, esperado):
    normalizados, errores = validar(**cambio)
    assert errores == {}
    assert normalizados[campo] == esperado


def test_los_errores_de_umbral_se_informan_todos_juntos():
    """CP-83 (EC-01): peso excesivo y texto de relleno en una sola respuesta."""
    _, errores = validar(peso="500", sintomas="a", diagnostico="asdf")
    assert set(errores) == {"peso", "sintomas", "diagnostico"}


# ------------------------------------------------------- advertencias (validador solo)
def referencia(peso, dias=None):
    return ReferenciaPeso(Decimal(peso), None if dias is None else HOY - timedelta(days=dias))


def avisos(peso, ref=None, dias_atras=0):
    normalizados = {"fecha": HOY - timedelta(days=dias_atras), "peso": Decimal(peso)}
    obtener = (lambda fecha: ref) if ref is not None else None
    return ValidacionRegistrosClinicos().advertencias(normalizados, obtener)


@pytest.mark.parametrize("peso,ref,hay_aviso", [
    pytest.param("55", referencia("3", 60), True, id="CP-84-U07-typo-3kg-hace-2-meses-a-55kg"),
    pytest.param("55", referencia("5", 1), True, id="CP-85-U07-typo-5kg-ayer-a-55kg"),
    pytest.param("4.5", referencia("3", 60), False, id="CP-86-U07-cachorro-creciendo-dentro-de-la-banda"),
    pytest.param("5.1", referencia("3", 60), False, id="CP-87-U07-limite-superior-exacto"),
    pytest.param("5.11", referencia("3", 60), True, id="CP-88-U07-apenas-sobre-el-limite"),
    pytest.param("5.5", referencia("5", 0), False, id="CP-89-U07-mismo-dia-limite-superior"),
    pytest.param("5.51", referencia("5", 0), True, id="CP-90-U07-mismo-dia-sobre-el-limite"),
    pytest.param("4.5", referencia("5", 0), False, id="CP-91-U07-mismo-dia-limite-inferior"),
    pytest.param("4.49", referencia("5", 0), True, id="CP-92-U07-mismo-dia-bajo-el-limite"),
    pytest.param("6", referencia("3", 2000), False, id="CP-93-U07-tope-maximo-limite-superior"),
    pytest.param("6.01", referencia("3", 2000), True, id="CP-94-U07-tope-maximo-sobre-el-limite"),
    pytest.param("1.5", referencia("3", 2000), False, id="CP-95-U07-tope-maximo-limite-inferior"),
    pytest.param("1.49", referencia("3", 2000), True, id="CP-96-U07-tope-maximo-bajo-el-limite"),
    pytest.param("13.6", referencia("6.8"), False, id="CP-97-U07-peso-del-alta-limite-superior"),
    pytest.param("13.7", referencia("6.8"), True, id="CP-98-U07-peso-del-alta-sobre-el-limite"),
])
def test_variacion_de_peso_respecto_del_ultimo_registro(peso, ref, hay_aviso):
    resultado = avisos(peso, ref)
    assert ("peso" in resultado) is hay_aviso
    assert "fecha" not in resultado


def test_el_aviso_de_variacion_informa_el_rango_esperado():
    """CP-99: el mensaje cita el peso ingresado, el de referencia y el rango."""
    mensaje = avisos("55", referencia("3", 60))["peso"]
    assert "55" in mensaje and "3 kg" in mensaje and "hace 60" in mensaje
    assert "5.10" in mensaje and "1.50" in mensaje


@pytest.mark.parametrize("peso,hay_aviso", [
    pytest.param("200", False, id="CP-100-U09-sin-referencia-limite"),
    pytest.param("200.5", True, id="CP-101-U09-sin-referencia-sobre-el-limite"),
])
def test_peso_muy_alto_sin_referencia(peso, hay_aviso):
    assert ("peso" in avisos(peso)) is hay_aviso


def test_peso_alto_consistente_con_la_referencia_no_avisa():
    """CP-102: un animal que ya pesaba 118 kg y hoy pesa 120 no genera aviso."""
    assert avisos("120", referencia("118", 10)) == {}


@pytest.mark.parametrize("dias,hay_aviso", [
    pytest.param(0, False, id="CP-103-U08-fecha-de-hoy"),
    pytest.param(30, False, id="CP-104-U08-fecha-en-el-limite"),
    pytest.param(31, True, id="CP-105-U08-fecha-apenas-antigua"),
])
def test_fecha_antigua(dias, hay_aviso):
    assert ("fecha" in avisos("5.2", dias_atras=dias)) is hay_aviso


# ------------------------------------------------------- servicio: confirmación
def consulta_previa(dias, peso, historia_id=1):
    return Consulta(id=0, historia_id=historia_id, veterinario_id=1,
                    fecha=HOY - timedelta(days=dias), peso=Decimal(peso),
                    sintomas="Control", diagnostico="Control", observaciones="")


def repo_con(*previas):
    repo = RepositorioEspia()
    for previa in previas:
        repo.guardar_consulta(previa)
    repo.llamadas_guardar = 0
    return repo


def datos(**cambios):
    d = datos_validos()
    d.update(cambios)
    return d


def test_dato_atipico_sin_confirmar_no_se_guarda():
    """CP-106 (U-07, EC-01): el rechazo conserva la entrada y no persiste nada."""
    repo = repo_con(consulta_previa(60, "3"))
    entrada = datos(peso="55")
    resultado = servicio_con(repo).registrar(1, entrada)
    assert resultado.estado == "requiere_confirmacion"
    assert set(resultado.advertencias) == {"peso"} and resultado.errores == {}
    assert resultado.consulta is None
    assert repo.llamadas_guardar == 0
    assert entrada["peso"] == "55"


def test_dato_atipico_confirmado_se_guarda():
    """CP-107."""
    repo = repo_con(consulta_previa(60, "3"))
    resultado = servicio_con(repo).registrar(1, datos(peso="55"), confirmado=True)
    assert resultado.estado == "creado"
    assert resultado.consulta.peso == Decimal("55")
    assert repo.llamadas_guardar == 1


def test_la_referencia_es_la_consulta_mas_reciente():
    """CP-108: 20 kg hace 5 días es la referencia (no los 3 kg de hace 200 días)."""
    repo = repo_con(consulta_previa(200, "3"), consulta_previa(5, "20"))
    assert servicio_con(repo).registrar(1, datos(peso="21")).estado == "creado"


def test_una_consulta_retroactiva_se_compara_con_la_anterior_a_su_fecha():
    """CP-109: carga de hace 20 días; compara con los 3 kg de hace 40 días, no con los 8 kg de hace 5."""
    repo = repo_con(consulta_previa(40, "3"), consulta_previa(5, "8"))
    fecha = (HOY - timedelta(days=20)).isoformat()
    assert servicio_con(repo).registrar(1, datos(fecha=fecha, peso="3.5")).estado == "creado"


def test_si_todas_las_consultas_son_posteriores_no_hay_referencia():
    """CP-110."""
    repo = repo_con(consulta_previa(5, "8"))
    fecha = (HOY - timedelta(days=20)).isoformat()
    assert servicio_con(repo).registrar(1, datos(fecha=fecha, peso="40")).estado == "creado"


def test_sin_consultas_se_compara_con_el_peso_del_alta():
    """CP-111: Luna se dio de alta con 6.8 kg; 14 kg supera el tope de +100 %."""
    resultado = servicio_con(RepositorioEspia()).registrar(1, datos(peso="14"))
    assert resultado.estado == "requiere_confirmacion"
    assert "registrado en el alta" in resultado.advertencias["peso"]


def test_fecha_antigua_pide_confirmacion():
    """CP-112."""
    entrada = datos(fecha=(HOY - timedelta(days=31)).isoformat())
    repo = RepositorioEspia()
    resultado = servicio_con(repo).registrar(1, entrada)
    assert resultado.estado == "requiere_confirmacion"
    assert set(resultado.advertencias) == {"fecha"}
    assert servicio_con(repo).registrar(1, entrada, confirmado=True).estado == "creado"


def test_las_advertencias_se_informan_todas_juntas():
    """CP-113."""
    entrada = datos(fecha=(HOY - timedelta(days=90)).isoformat(), peso="14")
    resultado = servicio_con(RepositorioEspia()).registrar(1, entrada)
    assert set(resultado.advertencias) == {"fecha", "peso"}


def test_un_error_tiene_prioridad_sobre_las_advertencias():
    """CP-114: peso > 300 kg es error aunque se confirme; no se guarda."""
    repo = RepositorioEspia()
    resultado = servicio_con(repo).registrar(1, datos(peso="500"), confirmado=True)
    assert resultado.estado == "invalido" and "peso" in resultado.errores
    assert repo.llamadas_guardar == 0


# ------------------------------------------------------- API
RUTA = "/api/mascotas/1/consultas"


def cliente():
    from app import crear_app
    return crear_app(RepositorioClinicoSQLite()).test_client()


def test_api_dato_atipico_responde_409_y_no_guarda():
    """CP-115."""
    c = cliente()
    r = c.post(RUTA, json=datos(peso="14"))
    assert r.status_code == 409
    assert set(r.get_json()["advertencias"]) == {"peso"}
    assert c.get(RUTA).get_json() == []


def test_api_confirmacion_explicita_guarda_con_201():
    """CP-116."""
    c = cliente()
    r = c.post(RUTA, json={**datos(peso="14"), "confirmar_atipicos": True})
    assert r.status_code == 201
    assert c.get("/api/mascotas/1").get_json()["peso_actual"] == "14"


@pytest.mark.parametrize("valor", ["true", 1, "on"], ids=["CP-117a-texto", "CP-117b-numero", "CP-117c-on"])
def test_api_solo_el_booleano_true_confirma(valor):
    """CP-117."""
    r = cliente().post(RUTA, json={**datos(peso="14"), "confirmar_atipicos": valor})
    assert r.status_code == 409


def test_api_peso_sobre_300_kg_responde_422_aun_confirmado():
    """CP-118."""
    r = cliente().post(RUTA, json={**datos(peso="301"), "confirmar_atipicos": True})
    assert r.status_code == 422
    assert "peso" in r.get_json()["errores"]
