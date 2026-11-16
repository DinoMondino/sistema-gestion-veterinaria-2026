"""Entidades necesarias para el slice HU-01."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass(frozen=True)
class Veterinario:
    id: int
    nombre: str

@dataclass(frozen=True)
class Mascota:
    id: int
    nombre: str
    especie: str
    peso_actual: Decimal

@dataclass(frozen=True)
class HistoriaClinica:
    id: int
    mascota_id: int

@dataclass(frozen=True)
class Consulta:
    id: int
    historia_id: int
    veterinario_id: int
    fecha: date
    peso: Decimal
    sintomas: str
    diagnostico: str
    observaciones: str = ""
