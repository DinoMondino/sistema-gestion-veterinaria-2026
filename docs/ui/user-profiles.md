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

### Escenario A — HU-01: Datos obligatorios incompletos o con formato inválido

El médico veterinario se encuentra registrando una nueva consulta clínica para el paciente Luna. Durante la carga de los datos, deja un campo obligatorio incompleto e ingresa un valor inválido en otro campo. Al seleccionar la opción de guardar la consulta, el sistema debe validar la información, impedir el almacenamiento del registro y señalar los campos que presentan errores, indicando el motivo de cada uno.

**Flujo de navegación:**

Pantalla: Nueva consulta
        ↓
        Completa datos
        ↓
        Intenta guardar
        ↓
Pantalla: Nueva consulta con errores de validación
        ↓
        Corrige los datos
        ↓
        Guarda correctamente

#### Escenario B (para HU-02 - Edición de Historial)

* **Narración del escenario:** El médico veterinario consulta el historial clínico de un paciente y selecciona una entrada previa que necesita ser corregida. Edita la información correspondiente, registra la justificación del cambio y confirma la modificación.
* **Flujo de Navegación:**
  Pantalla 1: Historial clínico
        ↓
        Selecciona una entrada existente
        ↓
Pantalla 2: Editar entrada del historial
        ↓
        Modifica los datos y registra la justificación
        ↓
        Confirma la edición
        ↓
Pantalla 3: Historial clínico actualizado
#### Escenario C (para HU-03 - Alerta de Interacción Medicamentosa)

* **Narración del escenario:** El médico veterinario se encuentra gestionando el tratamiento del paciente Luna y selecciona un nuevo medicamento para incorporarlo al tratamiento. El sistema detecta que existe una posible interacción con una medicación que el paciente ya tiene registrada. Antes de completar la prescripción, el sistema debe informar la interacción detectada y solicitar una decisión al veterinario.
* **Flujo de Navegación:**
  Pantalla: Prescripción / tratamiento
        ↓
        Selecciona medicamento
        ↓
Pantalla: Prescripción con alerta de interacción
        ↓
        Cancela o continúa
