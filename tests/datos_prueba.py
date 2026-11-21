"""Datos y dobles de prueba compartidos."""
from datetime import date

from src.aplicacion.servicio_registro import ServicioRegistroClinico
from src.aplicacion.validacion import ValidacionRegistrosClinicos
from src.infraestructura.repositorios import ErrorPersistencia, RepositorioClinicoEnMemoria


def datos_validos():
    return {
        "fecha": date.today().isoformat(),
        "peso": "5.2",
        "sintomas": "Fiebre",
        "diagnostico": "Control clínico",
        "observaciones": "Sin novedades",
    }


def servicio_con(repo):
    return ServicioRegistroClinico(repo, ValidacionRegistrosClinicos())


class RepositorioEspia(RepositorioClinicoEnMemoria):
    """Cuenta las llamadas a guardar_consulta para comprobar que un rechazo no persiste."""
    def __init__(self):
        super().__init__()
        self.llamadas_guardar = 0

    def guardar_consulta(self, consulta):
        self.llamadas_guardar += 1
        return super().guardar_consulta(consulta)


class RepositorioCaido(RepositorioClinicoEnMemoria):
    """Simula la caída de la base al guardar (EC-03)."""
    def guardar_consulta(self, consulta):
        raise ErrorPersistencia("base no disponible")
