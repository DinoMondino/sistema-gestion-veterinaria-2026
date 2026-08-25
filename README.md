# Sistema de gestión clínica veterinaria (Pequeños y grandes animales)
## Ingeniería de Software (2026)

## Integrantes
Modino, Maria Delfina
Sarmiento, Augusto
Olivera Villa, Julieta
---
## 1. Propuesta de proyecto
Sistema diseñado para unificar la gestión clínica y administrativa tanto de mascotas (pequeños animales) como de establecimientos de campo (grandes animales / producción). 

Funcionalidades principales:
  * Seguimiento clínico integral (peso, vacunas, patologías, medicaciones y procedimientos).
  * Correlación orientativa entre síntomas, patologías y tratamientos (con soporte en bases de datos como OMIA).
  * Control de interacciones medicamentosas, contraindicaciones y tiempos de carencia.
  * Planificación de tratamientos individuales y planes sanitarios masivos.
Beneficio: Funciona como soporte de trazabilidad, toma de decisiones y planificación adaptable a la heterogeneidad de las especies, aumentando la validez de los datos clínicos y la seguridad de los tratamientos.

---
## 2. Modelo de ciclo de vida
Se seleccionó un Modelo Incremental + Ágil:
Enfoque incremental: Permite entregar un núcleo administrativo y un MVP funcional rápido (pacientes, pesos, vacunas básicas) para validar con usuarios reales antes de incorporar módulos complejos (correlaciones o integraciones externas).
Gestión de riesgos: Aísla el riesgo técnico de la conexión externa con OMIA dejándola para iteraciones posteriores.
Prácticas ágiles: Se implementarán reuniones breves e iteraciones controladas para acompañar la evolución dinámica de los requerimientos en el dominio veterinario.

---
* [Ver el SRS completo y el Diagrama de Contexto detallado](docs/requirements/srs.md)
