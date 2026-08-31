# Especificación de Casos de Uso, Slices y Historias de Usuario
---
Proceso Seleccionado: Gestión Clínica e Historial
---
## Casos de uso
### CU-01 - Registrar y Actualizar Historial Clínico
Actor Principal: Médico Veterinario

Objetivo: Registrar una nueva atención médica para un paciente, actualizando de forma integrada su historial clínico (peso, síntomas, diagnóstico, vacunas, patologías, procedimientos y tratamientos).

Realiza: RF-01, RF-02, RF-03, RF-04, RF-05, RF-06, RF-10

Precondición: El médico veterinario ha iniciado sesión en el sistema con su cuenta habilitada y el paciente se encuentra registrado previamente.

Flujo Principal (Slice Básico):

1- El veterinario busca y selecciona al paciente en el sistema.

2- El sistema muestra la ficha e historial clínico cronológico base del paciente.

3- El veterinario ingresa los datos de la consulta: fecha, síntomas detectados, diagnóstico preliminar y observaciones en texto libre.

4- El veterinario ingresa el peso actual del paciente.

5- El veterinario registra los datos complementarios de la atención (vacunas aplicadas con número de lote y vencimiento, patologías asociadas, procedimientos realizados y medicaciones activas).

6- El sistema valida que todos los campos obligatorios cumplan con los formatos y rangos esperados (como fechas válidas y valores numéricos positivos para el peso).

7- El sistema almacena la información de la consulta, actualiza el historial cronológico y el peso vigente del paciente.

8- El sistema muestra un mensaje de confirmación del registro exitoso y actualiza la vista unificada del historial.

Postcondición: La consulta clínica y sus actualizaciones quedan guardadas y asociadas de forma permanente en el historial cronológico del paciente.

Slices Secundarios:

A1: Datos obligatorios incompletos o con formato inválido (vinculado a RF-11).

A2: Edición o corrección de una entrada previa en el historial clínico por parte del veterinario (vinculado a RF-08).

E1: Interrupción de la red durante el almacenamiento de la consulta.

CU-02 - Consultar Historial y Referencia Externa de Patologías
Actor Principal: Médico Veterinario

Objetivo: Consultar el historial cronológico unificado de un paciente y enlazar con la base de datos externa OMIA para verificar patologías.

Realiza: RF-07, RF-09, RF-12

Precondición: El paciente cuenta con registros previos en el sistema.

Flujo Principal (Slice Básico):

1- El veterinario selecciona al paciente y solicita ver su historial clínico completo.

2- El sistema recupera y muestra en una vista unificada las consultas, pesos, vacunas, patologías y procedimientos históricos.

3- El veterinario selecciona una patología específica y solicita consultar su referencia externa.

4- El sistema abre un enlace de lectura directa hacia la base de datos OMIA utilizando el término seleccionado.

5- El sistema genera de forma opcional gráficos de la evolución cronológica del peso del paciente.

Postcondición: El veterinario visualiza el historial consolidado y la referencia externa requerida sin alterar los datos del sistema.

Slices Secundarios:

A1: Sin conexión a internet al intentar acceder a la referencia externa OMIA.

A2: El paciente seleccionado no posee registros previos de peso para graficar.

### Historias de Usuario (Derivadas de Slices)
HU-01.A1 - Manejo de datos obligatorios incompletos o con formato inválido
Deriva de: CU-01, slice A1 (vinculado a RF-10 y RF-11)

Como Médico Veterinario,

quiero recibir una notificación precisa cuando intento guardar una consulta con campos obligatorios vacíos o datos con formato inválido,

para poder corregirlos y asegurar la integridad de la historia clínica sin perder la información cargada.

Criterios de Aceptación (GWT):

Given: El veterinario está completando el formulario de nueva consulta y escribe un valor negativo en el campo de peso o deja la fecha en blanco.

When: El veterinario presiona el botón "Guardar Consulta".

Then: El sistema rechaza el almacenamiento, resalta en rojo el campo con error y muestra un mensaje indicando con precisión el motivo del fallo.

HU-01.A2 - Edición de entradas previas en el historial clínico
Deriva de: CU-01, slice A2 (vinculado a RF-08)

Como Médico Veterinario,

quiero poder editar o corregir entradas previas dentro del historial clínico de un paciente,

para rectificar errores de tipeo o incorporar datos omitidos bajo mi validación exclusiva de rol.

Criterios de Aceptación (GWT):

Given: El veterinario con sesión activa visualiza el historial clínico y selecciona un registro de consulta previo de su autoría para modificar.

When: El veterinario edita la observación clínica y confirma los cambios.

Then: El sistema actualiza el registro seleccionado en la base de datos y refleja la modificación con un indicador de actualización en la vista del historial.