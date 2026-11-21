"""Controladores REST (contrato de implementacion-hu01.md). Se prueba la API, no la interfaz gráfica."""
from app import crear_app
from datos_prueba import RepositorioCaido, datos_validos
from src.infraestructura.repositorios import RepositorioClinicoSQLite

RUTA = "/api/mascotas/1/consultas"


def cliente(repo=None):
    return crear_app(repo or RepositorioClinicoSQLite()).test_client()


def test_contexto_de_la_mascota():
    """CP-51."""
    r = cliente().get("/api/mascotas/1")
    cuerpo = r.get_json()
    assert r.status_code == 200
    assert (cuerpo["nombre"], cuerpo["especie"], cuerpo["peso_actual"]) == ("Luna", "Perro", "6.8")


def test_mascota_inexistente_en_get():
    """CP-52."""
    assert cliente().get("/api/mascotas/999").status_code == 404
    assert cliente().get("/api/mascotas/999/consultas").status_code == 404


def test_guardar_consulta_valida_responde_201_y_aparece_en_el_listado():
    """CP-53 (criterio de aceptación: camino de éxito)."""
    c = cliente()
    r = c.post(RUTA, json=datos_validos())
    assert r.status_code == 201
    assert r.get_json()["consulta_id"] == 1
    listado = c.get(RUTA).get_json()
    assert [(x["id"], x["peso"], x["diagnostico"]) for x in listado] == [(1, "5.2", "Control clínico")]


def test_tras_guardar_el_contexto_muestra_el_nuevo_peso_vigente():
    """CP-54: Luna pasa de 6.8 a 5.84 kg cuando se guarda la consulta de hoy."""
    from datetime import date
    c = cliente()
    datos = datos_validos()
    datos.update(fecha=date.today().isoformat(), peso="5.84", diagnostico="Intoxicación")
    assert c.post(RUTA, json=datos).status_code == 201
    assert c.get("/api/mascotas/1").get_json()["peso_actual"] == "5.84"


def test_dato_invalido_responde_422_con_los_errores_y_no_guarda():
    """CP-55 (criterio de aceptación: peso negativo y fecha en blanco)."""
    c = cliente()
    datos = datos_validos()
    datos.update(peso="-5", fecha="")
    r = c.post(RUTA, json=datos)
    assert r.status_code == 422
    assert set(r.get_json()["errores"]) == {"fecha", "peso"}
    assert c.get(RUTA).get_json() == []


def test_el_rechazo_informa_todos_los_campos_en_una_respuesta():
    """CP-56 (EC-01)."""
    r = cliente().post(RUTA, json={})
    assert r.status_code == 422
    assert set(r.get_json()["errores"]) == {"fecha", "peso", "sintomas", "diagnostico"}


def test_cuerpo_que_no_es_un_objeto_json_responde_400():
    """CP-57."""
    c = cliente()
    assert c.post(RUTA, data="no es json", content_type="text/plain").status_code == 400
    assert c.post(RUTA, json=[1, 2]).status_code == 400


def test_guardar_en_mascota_inexistente_responde_404():
    """CP-58."""
    assert cliente().post("/api/mascotas/999/consultas", json=datos_validos()).status_code == 404


def test_falla_de_la_base_responde_503_con_aviso():
    """CP-59 (EC-03): respuesta controlada, no un error 500 sin explicación."""
    r = cliente(RepositorioCaido()).post(RUTA, json=datos_validos())
    assert r.status_code == 503
    assert "mantenimiento" in r.get_json()["error"]


def test_pagina_del_formulario():
    """CP-60."""
    c = cliente()
    assert c.get("/mascotas/1/nueva-consulta").status_code == 200
    assert c.get("/mascotas/999/nueva-consulta").status_code == 404
    assert c.get("/").status_code == 302


def test_sin_repositorio_explicito_la_app_usa_el_archivo_sqlite_configurado():
    """CP-61: la aplicación real persiste en SQLite (VETGESTION_DB) y no en memoria."""
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = os.path.join(carpeta, "vet.db")
        anterior = os.environ.get("VETGESTION_DB")
        os.environ["VETGESTION_DB"] = ruta
        try:
            c = crear_app().test_client()
            assert c.post(RUTA, json=datos_validos()).status_code == 201
            assert os.path.exists(ruta)
            otra_instancia = crear_app().test_client()      # simula reiniciar el servidor
            assert len(otra_instancia.get(RUTA).get_json()) == 1
        finally:
            if anterior is None:
                os.environ.pop("VETGESTION_DB")
            else:
                os.environ["VETGESTION_DB"] = anterior
