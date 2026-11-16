"""Punto de entrada de HU-01. Ejecutar: python app.py"""
from pathlib import Path
from flask import Flask, redirect, render_template, url_for
from src.api.controladores import crear_api
from src.aplicacion.servicio_registro import ServicioRegistroClinico
from src.aplicacion.validacion import ValidacionRegistrosClinicos
from src.infraestructura.repositorios import RepositorioClinicoEnMemoria

BASE = Path(__file__).resolve().parent

def crear_app(repositorio=None):
    app = Flask(__name__, template_folder=str(BASE / "templates"),
                static_folder=str(BASE / "static"))
    repo = repositorio if repositorio is not None else RepositorioClinicoEnMemoria()
    servicio = ServicioRegistroClinico(repo, ValidacionRegistrosClinicos())
    app.register_blueprint(crear_api(servicio, repo))

    @app.get("/")
    def inicio():
        return redirect(url_for("formulario", mascota_id=1))

    @app.get("/mascotas/<int:mascota_id>/nueva-consulta")
    def formulario(mascota_id):
        if repo.obtener_contexto(mascota_id) is None:
            return "Mascota no encontrada", 404
        return render_template("nueva_consulta.html", mascota_id=mascota_id)

    return app

if __name__ == "__main__":
    crear_app().run(port=5000, debug=True)
