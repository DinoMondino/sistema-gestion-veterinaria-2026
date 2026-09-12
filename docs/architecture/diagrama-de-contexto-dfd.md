---
title: Diagrama de contexto inicial (DFD Nivel 0)
---

# Diagrama de contexto — Sistema de Gestión Veterinaria

El sistema completo se representa como un único proceso (0), con sus entidades externas y los flujos de datos entre ambos, siguiendo la notación DFD Nivel 0 descripta en el instructivo de cátedra.

```mermaid
flowchart LR
    subgraph Izquierda [Actores de Gestión y Atención]
        SEC[Secretario/a o Recepcionista]
        VET[Médico/a Veterinario/a]
    end

    P((0 <br/> Gestionar Clínica <br/> Veterinaria))

    subgraph Derecha [Actores Externos y Clientes]
        DUE[Tutor/a de Mascota]
        OMIA[Base de Datos Externa OMIA]
    end

    %% Flujos Secretaría
    SEC ==>|Registra turnos, pagos, <br/> datos de tutores y mascotas| P
    P ==>|Confirma turnos <br/> y entrega comprobantes| SEC

    %% Flujos Veterinario
    VET ==>|Registra consultas, <br/> diagnósticos y vacunas| P
    P ==>|Provee historia clínica <br/> y calendario de vacunación| VET

    %% Flujos Tutor
    DUE ==>|Solicita turnos <br/> y consulta historial| P
    P ==>|Envía recordatorios, historias <br/> clínicas y comprobantes| DUE

    %% Flujos OMIA
    P ==>|Consulta patología <br/> y código genético| OMIA
    OMIA ==>|Devuelve información <br/> de referencia| P
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

# Descomposición funcional (DFD Nivel 1)

Descomponemos el proceso central 0 en 4 subprocesos lógicos:

1. Gestionar Turnos y Pacientes (maneja la agenda, admisión y registros iniciales).

2. Registrar Atención Clínica e Historial (maneja consultas, diagnósticos, vacunas y relación con OMIA).

3. Gestionar Pagos y Cobranzas (controla los pagos y comprobantes).

4. Administrar Usuarios y Permisos (gestión interna del sistema).

```mermaid
flowchart TD
    %% Actores Externos
    SEC[Secretario/a o Recepcionista]
    VET[Médico/a Veterinario/a]
    DUE[Tutor/a de Mascota]
    OMIA[Base de Datos Externa OMIA]

    %% Almacenes de Datos (Data Stores)
    D1[(D1 - Pacientes y Tutores)]
    D2[(D2 - Historias Clínicas)]
    D3[(D3 - Agenda y Turnos)]
    D4[(D4 - Pagos)]

    %% Procesos Nivel 1
    P1((1 <br/> Gestionar Turnos y Pacientes))
    P2((2 <br/> Registrar Atención Clínica))
    P3((3 <br/> Gestionar Pagos))
    P4((4 <br/> Consultar Referencia OMIA))

    %% Flujos Proceso 1 (Turnos y Pacientes)
    DUE -->|Solicitud de turno| P1
    SEC -->|Datos de tutor y mascota| P1
    P1 -->|Actualiza datos| D1
    P1 -->|Registra turno| D3
    P1 -->|Confirma turno y recordatorio| DUE
    P1 -->|Comprobante de agenda| SEC

    %% Flujos Proceso 2 (Atención Clínica e Historia)
    VET -->|Registra consulta y diagnóstico| P2
    D3 -->|Consulta turno asignado| P2
    D1 -->|Obtiene datos de mascota| P2
    P2 -->|Guarda evolución y vacunas| D2
    P2 -->|Provee historia clínica| VET
    P2 -->|Envía historia clínica actualizada| DUE

    %% Flujos Proceso 3 (Pagos)
    SEC -->|Registra pago de servicio| P3
    P3 -->|Registra transacción| D4
    P3 -->|Entrega comprobante de pago| SEC
    P3 -->|Informa estado de pago| DUE

    %% Flujos Proceso 4 (Consulta OMIA Externa)
    VET -->|Solicita código genético / patología| P4
    P4 -->|Consulta patología animal| OMIA
    OMIA -->|Devuelve datos de referencia| P4
    P4 -->|Provee referencia patológica| VET
```
