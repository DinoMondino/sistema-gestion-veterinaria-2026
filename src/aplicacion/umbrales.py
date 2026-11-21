"""Umbrales de integridad clínica de HU-01 (U-01 a U-09).

Un solo lugar, con nombre y trazabilidad. Los de tipo ERROR bloquean el guardado;
los de tipo ADVERTENCIA permiten guardar solo si el veterinario lo confirma.
"""
from dataclasses import dataclass
from decimal import Decimal

# Texto de relleno típico (comparado sin tildes, en minúsculas y sin espacios ni signos).
_RELLENOS = frozenset({
    "asd", "asdf", "asdfg", "asdasd", "qwerty", "qwe", "xxx", "xyz", "abc",
    "test", "prueba", "bla", "blabla", "nada", "ninguno", "nose", "sindatos",
    "lorem", "ipsum", "loremipsum",
})


@dataclass(frozen=True)
class Umbrales:
    # ERROR
    peso_max_kg: Decimal = Decimal("300")            # U-01
    peso_decimales_max: int = 2                      # U-02
    sintomas_min: int = 5                            # U-03
    diagnostico_min: int = 3                         # U-03
    letras_distintas_min: int = 3                    # U-04
    rellenos: frozenset = _RELLENOS                  # U-05
    sintomas_max: int = 1000                         # U-06
    diagnostico_max: int = 300                       # U-06
    observaciones_max: int = 2000                    # U-06
    # ADVERTENCIA (requieren confirmación)
    variacion_base: Decimal = Decimal("0.10")        # U-07: ±10 % el mismo día...
    variacion_por_dia: Decimal = Decimal("0.01")     # U-07: ...más 1 punto por día transcurrido
    variacion_max_suba: Decimal = Decimal("1.00")    # U-07: tope hacia arriba (+100 %)
    variacion_max_baja: Decimal = Decimal("0.50")    # U-07: tope hacia abajo (-50 %)
    dias_fecha_antigua: int = 30                     # U-08
    peso_alto_aviso_kg: Decimal = Decimal("200")     # U-09


UMBRALES = Umbrales()
