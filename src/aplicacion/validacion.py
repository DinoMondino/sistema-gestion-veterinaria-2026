"""RF-10 y RF-11. La pantalla NO contiene reglas de validación."""
from datetime import date
from decimal import Decimal, InvalidOperation

class ValidacionRegistrosClinicos:
    def validar(self, datos: dict) -> tuple[dict, dict[str, str]]:
        errores = {}
        normalizados = {}
        fecha_texto = str(datos.get("fecha") or "").strip()
        if not fecha_texto:
            errores["fecha"] = "Indicá la fecha de la consulta."
        else:
            try:
                fecha = date.fromisoformat(fecha_texto)
                if fecha > date.today():
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
            normalizados["peso"] = peso
        except (InvalidOperation, ValueError):
            errores["peso"] = "El peso debe ser un número mayor a 0 (en kg)."

        for campo, mensaje in (
            ("sintomas", "Describí los síntomas detectados."),
            ("diagnostico", "Ingresá el diagnóstico preliminar."),
        ):
            texto = str(datos.get(campo) or "").strip()
            if not texto:
                errores[campo] = mensaje
            else:
                normalizados[campo] = texto
        normalizados["observaciones"] = str(datos.get("observaciones") or "").strip()
        return normalizados, errores
