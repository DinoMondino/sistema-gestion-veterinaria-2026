"""RF-10 y RF-11. La pantalla NO contiene reglas de validación."""
import re
from datetime import date
from decimal import Decimal

# --- Umbrales (RF-10). Se ajustan acá y en ningún otro lugar. ---
PESO_MAXIMO_KG = Decimal("200")      # el SRS limita el alcance a mascotas/animales pequeños
PESO_DECIMALES_MAX = 2
FECHA_MINIMA = date(2000, 1, 1)
LARGO_MAXIMO = {"sintomas": 1000, "diagnostico": 200, "observaciones": 2000}

# [0-9] explícito: \d aceptaría dígitos de otros alfabetos.
_FORMATO_FECHA = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
_FORMATO_PESO = re.compile(r"[0-9]+(\.[0-9]+)?")


class ValidacionRegistrosClinicos:
    def validar(self, datos: dict) -> tuple[dict, dict[str, str]]:
        errores: dict[str, str] = {}
        normalizados: dict = {}

        self._validar_fecha(datos, errores, normalizados)
        self._validar_peso(datos, errores, normalizados)
        self._validar_texto(datos, "sintomas", True,
                            "Describí los síntomas detectados.", errores, normalizados)
        self._validar_texto(datos, "diagnostico", True,
                            "Ingresá el diagnóstico preliminar.", errores, normalizados)
        self._validar_texto(datos, "observaciones", False, "", errores, normalizados)
        return normalizados, errores

    @staticmethod
    def _validar_fecha(datos, errores, normalizados):
        texto = str(datos.get("fecha") or "").strip()
        if not texto:
            errores["fecha"] = "Indicá la fecha de la consulta."
            return
        # fromisoformat acepta variantes (p. ej. 20260101): se exige AAAA-MM-DD.
        if not _FORMATO_FECHA.fullmatch(texto):
            errores["fecha"] = "Ingresá una fecha válida (AAAA-MM-DD)."
            return
        try:
            fecha = date.fromisoformat(texto)
        except ValueError:
            errores["fecha"] = "Ingresá una fecha válida (AAAA-MM-DD)."
            return
        if fecha > date.today():
            errores["fecha"] = "La fecha no puede ser posterior a hoy."
        elif fecha < FECHA_MINIMA:
            errores["fecha"] = f"La fecha no puede ser anterior al {FECHA_MINIMA:%d/%m/%Y}."
        else:
            normalizados["fecha"] = fecha

    @staticmethod
    def _validar_peso(datos, errores, normalizados):
        texto = str(datos.get("peso") or "").strip().replace(",", ".")
        # El formato estricto descarta negativos, notación científica, NaN,
        # Infinity y guiones bajos (Decimal("1_0") sería 10).
        if not _FORMATO_PESO.fullmatch(texto):
            errores["peso"] = "El peso debe ser un número mayor a 0 (en kg)."
            return
        peso = Decimal(texto)
        if peso <= 0:
            errores["peso"] = "El peso debe ser un número mayor a 0 (en kg)."
        elif peso > PESO_MAXIMO_KG:
            errores["peso"] = f"El peso no puede superar {PESO_MAXIMO_KG} kg."
        elif max(0, -peso.normalize().as_tuple().exponent) > PESO_DECIMALES_MAX:
            errores["peso"] = f"El peso admite hasta {PESO_DECIMALES_MAX} decimales."
        else:
            normalizados["peso"] = peso

    @staticmethod
    def _validar_texto(datos, campo, obligatorio, mensaje, errores, normalizados):
        texto = str(datos.get(campo) or "").strip()
        if obligatorio and not texto:
            errores[campo] = mensaje
        elif len(texto) > LARGO_MAXIMO[campo]:
            errores[campo] = f"No puede superar los {LARGO_MAXIMO[campo]} caracteres."
        else:
            normalizados[campo] = texto
