"""Controlador REST: HTTP/JSON, sin reglas de negocio."""
from flask import Blueprint, jsonify, request
from src.aplicacion.servicio_registro import ServicioRegistroClinico
from src.infraestructura.repositorios import ErrorPersistencia, RepositorioClinico

def crear_api(servicio: ServicioRegistroClinico, repositorio: RepositorioClinico):
    api = Blueprint("api", __name__, url_prefix="/api")

    @api.get("/mascotas/<int:mascota_id>")
    def mascota(mascota_id):
        contexto = repositorio.obtener_contexto(mascota_id)
        if contexto is None:
            return jsonify(error="Mascota no encontrada."), 404
        mascota, historia = contexto
        return jsonify(id=mascota.id, nombre=mascota.nombre,
                       especie=mascota.especie, historia_id=historia.id,
                       peso_actual=str(mascota.peso_actual))

    @api.post("/mascotas/<int:mascota_id>/consultas")
    def guardar_consulta(mascota_id):
        datos = request.get_json(silent=True)
        if not isinstance(datos, dict):
            return jsonify(error="Se esperaba un objeto JSON."), 400
        try:
            resultado = servicio.registrar(mascota_id, datos)
        except ErrorPersistencia:
            return jsonify(error="El sistema está en mantenimiento. La consulta no se guardó; "
                                 "los datos cargados siguen en pantalla."), 503
        if resultado.estado == "no_encontrado":
            return jsonify(error="Mascota no encontrada."), 404
        if resultado.estado == "invalido":
            return jsonify(error="La consulta contiene datos inválidos.",
                           errores=resultado.errores), 422
        return jsonify(mensaje="Consulta guardada correctamente.",
                       consulta_id=resultado.consulta.id), 201

    @api.get("/mascotas/<int:mascota_id>/consultas")
    def listar_consultas(mascota_id):
        contexto = repositorio.obtener_contexto(mascota_id)
        if contexto is None:
            return jsonify(error="Mascota no encontrada."), 404
        _, historia = contexto
        consultas = repositorio.listar_consultas(historia.id)
        return jsonify([{"id": c.id, "fecha": c.fecha.isoformat(),
                         "peso": str(c.peso), "sintomas": c.sintomas,
                         "diagnostico": c.diagnostico, "observaciones": c.observaciones}
                        for c in consultas])

    return api
