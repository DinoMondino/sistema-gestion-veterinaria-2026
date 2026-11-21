"""RF-10 y RF-11 más los umbrales de integridad clínica (U-01 a U-09).

La pantalla NO contiene reglas de validación.
- validar():      errores que BLOQUEAN el guardado (HTTP 422).
- advertencias(): datos atípicos que se guardan solo con confirmación explícita (HTTP 409).
"""
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Callable

from src.aplicacion.umbrales import UMBRALES, Umbrales


@dataclass(frozen=True)
class ReferenciaPeso:
    """Último peso conocido. fecha=None si es el peso registrado en el alta de la mascota."""
    peso: Decimal
    fecha: date | None = None


def _plano(texto: str) -> str:
    """Minúsculas y sin tildes, para comparar texto."""
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


class ValidacionRegistrosClinicos:
    def __init__(self, umbrales: Umbrales = UMBRALES, hoy: Callable[[], date] = date.today):
        self._u = umbrales
        self._hoy = hoy

    # ---- Errores: bloquean el guardado ---------------------------------------------
    def validar(self, datos: dict) -> tuple[dict, dict[str, str]]:
        u = self._u
        errores = {}
        normalizados = {}
        fecha_texto = str(datos.get("fecha") or "").strip()
        if not fecha_texto:
            errores["fecha"] = "Indicá la fecha de la consulta."
        else:
            try:
                fecha = date.fromisoformat(fecha_texto)
                if fecha > self._hoy():
                    errores["fecha"] = "La fecha no puede ser posterior a hoy."
                else:
                    normalizados["fecha"] = fecha
            except ValueError:
                errores["fecha"] = "Ingresá una fecha válida (AAAA-MM-DD)."

        peso_texto = str(datos.get("peso") or "").strip().replace(",", ".")
        try:
            peso = Decimal(peso_texto)
            if not peso.is_finite() or peso <= 0:
                raise ValueError
        except (InvalidOperation, ValueError):
            errores["peso"] = "El peso debe ser un número mayor a 0 (en kg)."
        else:
            if peso > u.peso_max_kg:                                               # U-01
                errores["peso"] = f"El peso no puede superar {u.peso_max_kg} kg."
            elif peso.normalize().as_tuple().exponent < -u.peso_decimales_max:     # U-02
                errores["peso"] = f"El peso admite como máximo {u.peso_decimales_max} decimales."
            else:
                normalizados["peso"] = peso

        for campo, vacio, etiqueta, minimo, maximo in (
            ("sintomas", "Describí los síntomas detectados.", "Síntomas",
             u.sintomas_min, u.sintomas_max),
            ("diagnostico", "Ingresá el diagnóstico preliminar.", "Diagnóstico",
             u.diagnostico_min, u.diagnostico_max),
        ):
            texto = str(datos.get(campo) or "").strip()
            error = self._error_de_texto(texto, vacio, etiqueta, minimo, maximo)
            if error:
                errores[campo] = error
            else:
                normalizados[campo] = texto

        observaciones = str(datos.get("observaciones") or "").strip()
        if len(observaciones) > u.observaciones_max:                               # U-06
            errores["observaciones"] = (
                f"Las observaciones superan el máximo de {u.observaciones_max} caracteres.")
        else:
            normalizados["observaciones"] = observaciones
        return normalizados, errores

    def _error_de_texto(self, texto, vacio, etiqueta, minimo, maximo):
        u = self._u
        if not texto:
            return vacio
        if len(texto) < minimo:                                                    # U-03
            return f"{etiqueta}: escribí al menos {minimo} caracteres."
        if len(texto) > maximo:                                                    # U-06
            return f"{etiqueta}: el máximo es de {maximo} caracteres."
        plano = _plano(texto)
        letras = {c for c in plano if c.isalpha()}
        if len(letras) < u.letras_distintas_min or re.sub(r"[^a-z0-9]", "", plano) in u.rellenos:
            return f"{etiqueta}: parece texto de relleno, describilo con palabras."   # U-04 / U-05
        return None

    # ---- Advertencias: se guardan solo con confirmación ---------------------------
    def advertencias(self, normalizados: dict,
                     obtener_referencia: Callable[[date], ReferenciaPeso | None] | None = None
                     ) -> dict[str, str]:
        """Recibe datos YA validados. obtener_referencia(fecha) devuelve el peso de referencia."""
        avisos = {}
        fecha = normalizados["fecha"]
        dias_atras = (self._hoy() - fecha).days
        if dias_atras > self._u.dias_fecha_antigua:                                # U-08
            avisos["fecha"] = (f"La fecha es de hace {dias_atras} día(s). "
                               "Confirmá que no es un error de día, mes o año.")
        aviso_peso = self._aviso_de_peso(normalizados["peso"], fecha, obtener_referencia)
        if aviso_peso:
            avisos["peso"] = aviso_peso
        return avisos

    def _aviso_de_peso(self, peso, fecha, obtener_referencia):
        u = self._u
        ref = obtener_referencia(fecha) if obtener_referencia else None
        if ref is None:
            if peso > u.peso_alto_aviso_kg:                                        # U-09
                return (f"{peso} kg es un peso muy alto para una mascota. "
                        "Confirmá que no es un error de tipeo.")
            return None
        if ref.fecha is None:                                                      # U-07
            tolerancia = u.variacion_max_suba
            cuando = "registrado en el alta"
        else:
            dias = max(0, (fecha - ref.fecha).days)
            tolerancia = min(u.variacion_base + u.variacion_por_dia * dias, u.variacion_max_suba)
            cuando = f"hace {dias} día(s)"
        minimo = ref.peso * (1 - min(tolerancia, u.variacion_max_baja))
        maximo = ref.peso * (1 + tolerancia)
        if minimo <= peso <= maximo:
            return None
        return (f"El peso ({peso} kg) se aleja del último registrado ({ref.peso} kg, {cuando}). "
                f"Se esperaba entre {minimo:.2f} y {maximo:.2f} kg. Confirmá que es correcto.")
