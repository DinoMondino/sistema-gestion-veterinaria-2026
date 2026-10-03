### 1\. Criterios Generales para el Maquetado de Interfaz

Antes de generar el código HTML/CSS, definimos las decisiones tecnológicas y de diseño que guiarán la creación de las pantallas:

* **Tipo de sistema:** Aplicación Web Responsiva (SaaS) orientada primariamente a escritorio/tablet para consultorio clínico veterinario.
* **Lenguajes y tecnologías a utilizar para el maquetado:**
  * **HTML + python
* **Criterios de diseño UX/UI y Ergonomía:**
  * **Principios de Nielsen:** Visibilidad del estado del sistema, lenguaje claro del dominio veterinario (no jerga informática), prevención de errores, consistencia e indicadores explícitos de estado.
  * **Carga cognitiva mínima:** Organización jerárquica con patrones de información colapsables/pestañas para no saturar la vista durante la atención directa.
  * **Contraste y Accesibilidad (WCAG AA):** Tipografía legible, botones con áreas de clic amplias (Ley de Fitts) y contraste cromático adecuado (alertas rojas/amarillas destacadas para riesgos de salud/errores).

---

## Perfil de usuario

### Médico Veterinario

**Quién es:**
El médico veterinario es el actor principal de los casos de uso trabajados en esta Parte B. Es responsable de registrar y editar información de las historias clínicas, consultar la evolución clínica de los pacientes y gestionar tratamientos y prescripciones.

**Objetivo con el sistema:**
Registrar y consultar información clínica de los pacientes, mantener actualizado el historial clínico y gestionar tratamientos y prescripciones, incluyendo la detección de posibles interacciones medicamentosas.

**Contexto de uso:**
El sistema se utiliza como una aplicación web dentro del contexto de gestión clínica veterinaria. El TP1 establece que el médico veterinario interactúa directamente con el sistema para registrar atenciones, consultar historiales, editar entradas y gestionar tratamientos.

**Nivel de conocimiento técnico:**
El TP1 no especifica un nivel de conocimiento técnico del usuario. Por este motivo, no se incorpora una caracterización adicional del nivel técnico en este perfil.

**Limitaciones o frustraciones consideradas:**
El TP1 no define limitaciones personales, condiciones físicas ni frustraciones específicas del médico veterinario. Por lo tanto, no se incorporan características adicionales que no puedan justificarse a partir de la documentación del proyecto.

### Criterios de diseño derivados del perfil

A partir de las tareas establecidas en las historias de usuario, la interfaz debe priorizar:

* Presentar claramente el estado de las operaciones realizadas.
* Utilizar terminología relacionada con la gestión clínica veterinaria.
* Evitar errores mediante validaciones antes de almacenar información.
* Mostrar mensajes de error específicos y comprensibles.
* Permitir cancelar o corregir una operación cuando corresponda.
* Mantener visibles los datos relevantes del paciente durante las tareas clínicas.
* Mantener una estructura consistente entre las diferentes pantallas.


---

### 3\. Evaluación de Historias de Usuario (TP1) y Cuestión de Requerimiento de Interfaz

Revisando el alcance del TP1 (`slices.md`), las Historias de Usuario desarrolladas pertenecientes a los Casos de Uso 2.0 son:

1. **HU-01 (Manejo de datos obligatorios incompletos o con formato inválido):**
  * *¿Requiere Interfaz?:* **SÍ.** Se manifiesta en la pantalla de registro de consulta clínica cuando el usuario ingresa un valor erróneo o deja campos requeridos vacíos.
2. **HU-02 (Edición de entradas previas en el historial clínico):**
  * *¿Requiere Interfaz?:* **SÍ.** Se manifiesta en la vista unificada del historial clínico al habilitar el flujo/modal de modificación de observaciones y mostrar el distintivo de edición.
3. **HU-03 (Notificación de alerta por interacción medicamentosa):**
  * *¿Requiere Interfaz?:* **SÍ.** Se manifiesta mediante un diálogo modal/banner de alerta crítica cuando se intenta prescribir un fármaco incompatible.

*Todas las historias desarrolladas en el TP1 requieren maquetado de interfaz.*

---

### 4\. Escenarios de Uso y Flujos de Navegación

#### Escenario A (para HU-01 - Validación de Errores)

* **Narración del escenario:** El Dr. Veterinario está registrando de prisa una consulta de urgencia para el paciente "Firmeza". Al presionar "Guardar Consulta", olvidó ingresar la fecha y cargó un valor negativo (-2.5 kg) en el campo de peso. El sistema debe rechazar el envío sin limpiar la pantalla, resaltar visualmente en rojo los campos con error y mostrar un mensaje preciso.
* **Flujo de Navegación:**
  1. *Pantalla 1 (Ingreso de datos):* Formulario de Registro de Atención Clínica (`CU-01`).
  2. *Acción:* Clic en "Guardar Consulta".
  3. *Pantalla 1 (Estado con Error - HU-01):* Misma pantalla con campos resaltados en rojo, banderas de error bajo los insumos inválidos y banner superior descriptivo.

#### Escenario B (para HU-02 - Edición de Historial)

* **Narración del escenario:** El Dr. Veterinario revisa el historial clínico de "Firmeza" y advierte que en la consulta de la semana pasada cometió un error de tipeo en las observaciones del diagnóstico. Hace clic en "Editar Registro", corrige la observación y guarda. El sistema actualiza el registro y muestra la etiqueta "Editado por profesional" con fecha y hora.
* **Flujo de Navegación:**
  1. *Pantalla 2 (Consulta):* Vista Consolidada del Historial Clínico (`CU-02`).
  2. *Acción:* Clic en el botón "Editar" en la entrada previa.
  3. *Pantalla 2 (Panel/Modal de Edición - HU-02):* Despliegue de formulario de edición con justificación de cambio.
  4. *Pantalla 2 (Resultado):* Vista del historial actualizado con badge visual de auditoría.

#### Escenario C (para HU-03 - Alerta de Interacción Medicamentosa)

* **Narración del escenario:** Durante la consulta clínica, el veterinario decide agregar un AINE (antiinflamatorio) al tratamiento del paciente. El sistema detecta que el paciente ya tiene activo un tratamiento con corticoides. Al intentar confirmar la prescripción, el sistema interrumpe la acción desplegando un modal de advertencia crítica detallando el riesgo clínico e interacciones, solicitando justificar o cancelar.
* **Flujo de Navegación:**
  1. *Pantalla 3 (Prescripción):* Módulo de Tratamientos y Prescripción de Medicación (`CU-03`).
  2. *Acción:* Selección del fármaco en conflicto y clic en "Agregar Tratamiento".
  3. *Pantalla 3 (Modal de Alerta - HU-03):* Superposición de modal crítico con detalles de interacción medicamentosa y opciones de "Cancelar" o "Confirmar con Justificación".</dialog></mark></fieldset></nav></header></article></section></main>
