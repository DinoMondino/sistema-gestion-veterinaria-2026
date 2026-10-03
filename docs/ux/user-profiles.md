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

### 2\. Perfiles de Usuario (User Personas del TP1)

Apoyados directamente en los roles definidos en el `srs.md` del TP1:

#### Perfil 1: Médico Veterinario (Actor Principal de las HU del TP1)

* **Quién es:** Profesional de la salud animal responsable del diagnóstico, tratamiento y evolución de los pacientes.
* **Objetivo con el sistema:** Registrar la atención médica, consultar historiales, actualizar pesos/vacunas y prescribir medicación con la mayor rapidez y precisión posible.
* **Contexto de uso:** Consultorio o sala de examinación clínica, frente a la computadora o tablet. 
* **Frustraciones:** Perder datos ingresados por errores de validación o no enterarse a tiempo de incompatibilidades medicamentosas.


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
