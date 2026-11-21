"""Caso de uso: coordina el alta solo si la validación es exitosa y los datos atípicos están confirmados."""
from dataclasses import dataclass, field
from datetime import date
from src.aplicacion.validacion import ReferenciaPeso, ValidacionRegistrosClinicos
from src.dominio.entidades import Consulta
from src.infraestructura.repositorios import RepositorioClinico


@dataclass(frozen=True)
class ResultadoRegistro:
    """estado: creado | invalido | requiere_confirmacion | no_encontrado"""
    estado: str
    errores: dict[str, str]
    consulta: Consulta | None = None
    advertencias: dict[str, str] = field(default_factory=dict)


class ServicioRegistroClinico:
    def __init__(self, repositorio: RepositorioClinico, validador: ValidacionRegistrosClinicos):
        self.repositorio = repositorio
        self.validador = validador

    def registrar(self, mascota_id: int, datos: dict, confirmado: bool = False) -> ResultadoRegistro:
        contexto = self.repositorio.obtener_contexto(mascota_id)
        if contexto is None:
            return ResultadoRegistro("no_encontrado", {})
        mascota, historia = contexto
        normalizados, errores = self.validador.validar(datos)
        if errores:
            return ResultadoRegistro("invalido", errores)
        avisos = self.validador.advertencias(
            normalizados, lambda fecha: self._referencia_de_peso(mascota, historia, fecha))
        if avisos and not confirmado:
            return ResultadoRegistro("requiere_confirmacion", {}, None, avisos)
        # Autenticación real fuera del alcance del TP4: profesional fijo de demostración.
        consulta = Consulta(id=0, historia_id=historia.id, veterinario_id=1, **normalizados)
        creada = self.repositorio.guardar_consulta(consulta)
        return ResultadoRegistro("creado", {}, creada)

    def _referencia_de_peso(self, mascota, historia, fecha: date) -> ReferenciaPeso | None:
        """Peso de la consulta más reciente anterior (o igual) a la fecha indicada.
        Sin consultas: el peso del alta. Si todas las consultas son posteriores: sin referencia."""
        consultas = self.repositorio.listar_consultas(historia.id)
        previas = [c for c in consultas if c.fecha <= fecha]    # listar_consultas ya viene ordenada
        if previas:
            return ReferenciaPeso(previas[0].peso, previas[0].fecha)
        if not consultas:
            return ReferenciaPeso(mascota.peso_actual)
        return None
