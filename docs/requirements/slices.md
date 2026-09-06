# Especificación de Casos de Uso, Slices y Historias de Usuario
---
Proceso Seleccionado: Gestión Clínica e Historial

La elección de este proceso responde a nuestra estrategia incremental, representa el núcleo de valor del sistema de software veterinario. El módulo concentra complejidad de dominio (la diversidad de datos clínicos, el seguimiento temporal de pesos, la aplicación de vacunas y las reglas de validación sanitaria). Al acotar el desarrollo profundo a este único proceso central, se evita el riesgo de sobrediseño y se garantiza un nivel de calidad técnico óptimo para un equipo reducido en el marco de un cuatrimestre.
---
## Casos de Uso Esenciales
### CU-01 - Registrar Atención y Evolución Clínica
Actor Principal: Médico Veterinario

Objetivo: Registrar una nueva atención médica estructurada para un paciente, actualizando de forma integrada su historial clínico (síntomas, diagnóstico, vacunas, patologías, procedimientos) y su peso actual.

Realiza: RF-01, RF-02, RF-03, RF-04, RF-05, RF-10

Precondición: El médico veterinario ha iniciado sesión en el sistema con su cuenta habilitada y el paciente se encuentra registrado previamente.

Flujo Principal (Slice Básico):

El veterinario busca y selecciona al paciente en el sistema.

El sistema muestra la ficha e historial clínico cronológico base del paciente.

El veterinario ingresa los datos de la consulta: fecha, síntomas detectados, diagnóstico preliminar y observaciones en texto libre.

El veterinario ingresa el peso actual del paciente y registra los datos complementarios de la atención (vacunas aplicadas con número de lote y vencimiento, patologías asociadas y procedimientos realizados).

El sistema valida que todos los campos obligatorios cumplan con los formatos y rangos esperados.

El sistema almacena la información de la consulta, actualiza el historial cronológico y el peso vigente del paciente.

El sistema muestra un mensaje de confirmación del registro exitoso y actualiza la vista unificada del historial.

Postcondición: La consulta clínica y sus actualizaciones quedan guardadas y asociadas de forma permanente en el historial cronológico del paciente.

Slices Secundarios:

A1: Datos obligatorios incompletos o con formato inválido (vinculado a RF-11).

A2: Edición o corrección de una entrada previa en el historial clínico por parte del veterinario (vinculado a RF-08).

E1: Interrupción de la red durante el almacenamiento de la consulta.

### CU-02 - Consultar Historial Clínico
Actor Principal: Médico Veterinario

Objetivo: Visualizar el historial cronológico completo de un paciente en una vista consolidada y generar gráficos o reportes de la evolución temporal de su peso.

Realiza: RF-07, RF-12

Precondición: El paciente cuenta con registros históricos previos en el sistema.

Flujo Principal (Slice Básico):

El veterinario selecciona al paciente y solicita ver su historial clínico completo.

El sistema recupera y muestra en una vista unificada las consultas, pesos, vacunas, patologías y procedimientos históricos.

El veterinario solicita visualizar la evolución temporal del peso del paciente.

El sistema genera y muestra un gráfico o reporte tabular con el historial de pesos registrados a lo largo del tiempo.

Postcondición: El veterinario visualiza el historial consolidado y la evolución métrica del paciente sin alterar los datos del sistema.

Slices Secundarios:

A1: El paciente seleccionado no posee registros previos suficientes para generar el gráfico de peso.

E1: Error de renderizado del componente gráfico en la interfaz.

CU-03 - Gestionar Tratamientos y Validar Alertas Sanitarias
Actor Principal: Médico Veterinario

Objetivo: Registrar las medicaciones activas del paciente y evaluar alertas automáticas ante posibles contraindicaciones o interacciones medicamentosas elementales.

Realiza: RF-06, RF-10, RF-11

Precondición: El médico veterinario se encuentra dentro de una consulta clínica activa y cuenta con el listado de fármacos disponibles.

Flujo Principal (Slice Básico):

El veterinario selecciona la opción de prescribir medicación o suplementación en el plan de tratamiento del paciente.

El sistema verifica el listado de fármacos activos actuales del paciente.

El sistema valida las reglas de negocio y descarta la existencia de interacciones críticas.

El sistema registra la nueva medicación activa en el plan de tratamiento.

El sistema confirma el almacenamiento exitoso de la prescripción.

Postcondición: La medicación queda asociada formalmente al plan de tratamiento activo del paciente.

Slices Secundarios:

A1: Detección automática de una posible interacción medicamentosa elemental o contraindicación (RF-10).

A2: Intento de registrar un fármaco con fecha de vigencia vencida o datos incompletos.

Historias de Usuario (Derivadas de Slices)
HU-01 - Manejo de datos obligatorios incompletos o con formato inválido
Deriva de: CU-01, slice A1 (RF-10 y RF-11)

Como Médico Veterinario,

quiero recibir una notificación precisa cuando intento guardar una consulta con campos obligatorios vacíos o datos con formato inválido,

para poder corregirlos y asegurar la integridad de la historia clínica sin perder la información cargada.

Criterios de Aceptación (GWT):

Given: El veterinario está completando el formulario de nueva consulta y escribe un valor negativo en el campo de peso o deja la fecha en blanco.

When: El veterinario presiona el botón "Guardar Consulta".

Then: El sistema rechaza el almacenamiento, resalta en rojo el campo con error y muestra un mensaje indicando con precisión el motivo del fallo.

HU-02 - Edición de entradas previas en el historial clínico
Deriva de: CU-01, slice A2 (RF-08)

Como Médico Veterinario,

quiero poder editar o corregir entradas previas dentro del historial clínico de un paciente,

para rectificar errores de tipeo o incorporar datos omitidos bajo mi validación exclusiva de rol.

Criterios de Aceptación (GWT):

Given: El veterinario con sesión activa visualiza el historial clínico y selecciona un registro de consulta previo de su autoría para modificar.

When: El veterinario edita la observación clínica y confirma los cambios.

Then: El sistema actualiza el registro seleccionado en la base de datos y refleja la modificación con un indicador de actualización en la vista del historial.

HU-03 - Notificación de alerta por interacción medicamentosa
Deriva de: CU-03, slice A1 (RF-10)

Como Médico Veterinario,

quiero visualizar una advertencia clara cuando el sistema detecta una interacción o contraindicación entre la medicación recetada y los fármacos activos del paciente,

para reevaluar la prescripción y prevenir riesgos clínicos durante el tratamiento.

Criterios de Aceptación (GWT):

Given: El paciente tiene una medicación activa registrada que genera conflicto con el nuevo fármaco que el veterinario intenta prescribir.

When: El veterinario selecciona y confirma la nueva prescripción en el sistema.

Then: El sistema despliega una alerta visual detallando la incompatibilidad detectada, permitiendo al profesional justificar su decisión o cancelar la acción.