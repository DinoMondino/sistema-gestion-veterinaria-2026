"""Caso de uso: coordina el alta solo si toda la validación es exitosa."""
from dataclasses import dataclass
from src.aplicacion.validacion import ValidacionRegistrosClinicos
from src.dominio.entidades import Consulta
from src.infraestructura.repositorios import RepositorioClinico

@dataclass(frozen=True)
class ResultadoRegistro:
    estado: str
    errores: dict[str, str]
    consulta: Consulta | None = None

class ServicioRegistroClinico:
    def __init__(self, repositorio: RepositorioClinico, validador: ValidacionRegistrosClinicos):
        self.repositorio = repositorio
        self.validador = validador

    def registrar(self, mascota_id: int, datos: dict) -> ResultadoRegistro:
        contexto = self.repositorio.obtener_contexto(mascota_id)
        if contexto is None:
            return ResultadoRegistro("no_encontrado", {})
        normalizados, errores = self.validador.validar(datos)
        if errores:
            return ResultadoRegistro("invalido", errores)
        _, historia = contexto
        # Autenticación real fuera del alcance del TP4: profesional fijo de demostración.
        consulta = Consulta(id=0, historia_id=historia.id, veterinario_id=1,
                            **normalizados)
        creada = self.repositorio.guardar_consulta(consulta)
        return ResultadoRegistro("creado", {}, creada)
