---
title: Diagrama de contexto inicial (DFD Nivel 0)
---

# Diagrama de contexto — Sistema de Gestión Veterinaria

El sistema completo se representa como un único proceso (0), con sus entidades externas y los flujos de datos entre ambos, siguiendo la notación DFD Nivel 0 descripta en el instructivo de cátedra.

```mermaid
flowchart TD
    P((0 <br/> Gestionar Clínica <br/> Veterinaria))

    SEC[Secretario/a o Recepcionista]
    VET[Médico/a Veterinario/a]
    DUE[Tutor/a de Mascota]
    OMIA[Base de Datos Externa OMIA]

    %% Flujos de Secretario/a
    SEC -->|Registra turnos, pagos, datos de tutores y mascotas| P
    P -->|Confirma turnos y entrega comprobantes de pago| SEC

    %% Flujos de Veterinario/a
    VET -->|Registra consultas, diagnósticos, vacunas aplicadas| P
    P -->|Provee historia clínica y calendario de vacunación| VET

    %% Flujos de Tutor/a de Mascota
    DUE -->|Solicita turnos y consulta historia clínica| P
    P -->|Envía recordatorios, historias clínicas y comprobantes| DUE

    %% Flujos de BD Externa OMIA
    P -->|Consulta patología y código genético animal| OMIA
    OMIA -->|Provee información de referencia de la patología| P
```

**Entidades externas identificadas:**

- **Secretario/a o Recepcionista**: gestiona turnos, datos de contacto de tutores/mascotas y pagos.
- **Médico/a Veterinario/a**: registra consultas, diagnósticos y aplicaciones de vacunas; consulta patologías.
- **Tutor/a de Mascota**: solicita turnos y consulta información de su(s) mascota(s).
- **Base de Datos Externa OMIA**: fuente de referencia externa sobre patologías y código genético animal (consulta de solo lectura, no se sincroniza como base propia — ver justificación en `docs/requirements/srs.md`, sección 1.6).

> 

## Checklist de verificación (según el instructivo)

- [x] Hay un único proceso, numerado 0, nombrado con verbo + objeto ("Gestionar Clínica Veterinaria").
- [x] No aparecen almacenes (corresponden a Nivel 1, fuera de alcance de esta materia).
- [x] Las 4 entidades externas tienen nombres significativos y concretos (dentro del rango de 4-6 que sugiere el instructivo).
- [x] No hay flujos sin etiqueta.
- [x] Todos los terminadores se conectan únicamente al proceso central, no entre sí.
- [x] Cada flujo tiene su contraparte lógica en sentido inverso (ej. el/la secretario/a registra pagos y recibe comprobantes; el sistema consulta OMIA y recibe la información de vuelta).
- [x] El diagrama está en un bloque ` ```mermaid ` dentro de este `.md`, no como imagen.
