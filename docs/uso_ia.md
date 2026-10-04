## Entrega TP1

Uso crítico de IA:

Para la realización del TP1 se utilizaron herramientas de inteligencia artificial generativa como apoyo para la estructuración del canvas de descubrimiento y la redacción inicial de los artefactos del SRS. La IA se utilizó como herramienta de asistencia metodológica, revisión y discusión, y no como sustituto del análisis realizado por el grupo.

Herramientas utilizadas y tarea realizada:

Inicialmente se utilizó Claude (Anthropic), mediante su interfaz de chat, para organizar una idea de proyecto que se encontraba planteada de manera preliminar y desordenada. La propuesta inicial consistía en un sistema de gestión para una clínica veterinaria, con una lista de funcionalidades que incluía calendario y registro de vacunación, registro de pagos, historia clínica e integración con la base de datos OMIA.
Se solicitó a la IA que ayudara a estructurar esta propuesta, identificara funcionalidades que pudieran resultar poco realistas para un proyecto desarrollado por 3 personas durante un cuatrimestre, sugiriera funcionalidades faltantes, organizara las responsabilidades según los distintos roles de usuario y elaborara borradores iniciales de los principales artefactos solicitados en el TP1.

A partir de esta interacción se generaron propuestas para la visión y alcance del SRS, identificación de stakeholders y riesgos, diagrama de contexto DFD, modelo de dominio conceptual, casos de uso en formato Cockburn, historias de usuario con criterios de aceptación Given-When-Then y atributos de calidad basados en ISO 25010.
Posteriormente, durante la revisión y desarrollo del trabajo, se utilizó Gemini Notebook como asistente metodológico para contrastar los borradores y diagramas con las consignas y la teoría oficial de la materia. Esta segunda etapa permitió revisar críticamente las propuestas iniciales y detectar inconsistencias de nomenclatura, modelado y especificación.

Qué generó la IA:

Entre las principales propuestas generadas se encontró una primera delimitación del alcance del proyecto. Se recomendó excluir del MVP funcionalidades como la facturación electrónica vinculada con AFIP y la gestión de inventario de insumos, debido a que podían aumentar considerablemente el alcance para el tiempo y tamaño del equipo disponible.
También se reformuló la integración con OMIA. En lugar de plantearla como una sincronización completa con la base externa, se propuso inicialmente un enfoque más acotado de consulta o enlace de información. Esta modificación se consideró más realista para el alcance del proyecto y permitió evitar asumir una integración técnica que no estaba justificada por los requerimientos del trabajo.
La IA también propuso una primera identificación de stakeholders, una organización de las funcionalidades según los roles de Tutor/a de Mascota, Secretario/a o Recepcionista y Veterinario/a, seis casos de uso, ocho historias de usuario con criterios de aceptación y escenarios de calidad asociados a distintos atributos de ISO 25010.

Qué se modificó, aceptó o descartó:

El resultado generado por la IA no fue incorporado directamente al trabajo. Cada propuesta fue revisada por el grupo y contrastada con las consignas de la cátedra y con las necesidades reales del proyecto.
En primer lugar, se aceptó la recomendación de acotar el alcance del MVP. Se decidió dejar fuera la facturación electrónica/AFIP y la gestión de inventario de insumos porque no resultaban esenciales para el objetivo principal del proyecto y podían hacer que el desarrollo fuera poco viable dentro de un cuatrimestre y con un equipo reducido. La decisión permitió concentrar el trabajo en las funcionalidades centrales de gestión de una clínica veterinaria.
Por el momento se aceptó el enfoque acotado para OMIA, pero no como una integración completa. Se consideró más apropiado plantearla como una consulta o acceso de solo lectura a información externa, evitando que el proyecto dependiera de una sincronización o API que no estaba contemplada como requisito principal. De esta manera, la funcionalidad conserva valor para el usuario sin introducir una dependencia técnica innecesaria.
También se revisó y unificó la terminología de los roles. En los primeros borradores aparecían expresiones como "Dueño de mascota", "DuenioMascota" y "Secretaria". Luego de la revisión se decidió utilizar de manera consistente Tutor/a de Mascota y Secretario/a o Recepcionista, utilizando TutorMascota y SecretariaRecepcionista en el modelo. Esta modificación se realizó para evitar inconsistencias entre el texto, los diagramas y el modelo conceptual.

En el DFD de nivel 0 también se modificó el nombre del proceso central. La propuesta inicial utilizaba "Sistema de Gestión Veterinaria", pero al contrastarla con la teoría de la cátedra se detectó que el proceso debía expresarse como una acción mediante la estructura verbo + objeto y que no correspondía utilizar la palabra "Sistema". Por este motivo se reemplazó por "0: Gestionar Clínica Veterinaria".
El modelo de dominio conceptual también fue revisado en lugar de aceptar directamente las multiplicidades propuestas por la IA. Se decidió representar que cada Mascota posee una única HistoriaClinica, estableciendo una relación 1 a 1, mientras que una HistoriaClinica puede registrar 0..* Consultas. Esta modificación representa mejor el funcionamiento esperado del dominio y evita relaciones genéricas que no reflejaban correctamente la lógica del proyecto.

Por último, se revisaron los escenarios de calidad. Las primeras propuestas contenían expresiones generales como "el sistema debe ser rápido", que no permitían verificar objetivamente si el requisito se cumplía. El grupo decidió reformular estos escenarios siguiendo la estructura de seis elementos trabajada en la materia: Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida. De esta manera, se incorporaron métricas verificables, como tiempos de respuesta inferiores a determinados valores y límites de tiempo ante fallos de servicios externos.

Errores e imprecisiones detectados:

El principal aprendizaje del uso de IA fue que las respuestas generadas podían ser técnicamente plausibles, pero no necesariamente coincidir con las reglas específicas de la materia ni con las necesidades concretas del proyecto.
Durante la revisión se detectaron varias imprecisiones.
Una de ellas fue la inconsistencia en los nombres de los roles, ya que diferentes artefactos utilizaban denominaciones distintas para referirse al mismo actor. Esto podía generar ambigüedad y problemas de consistencia entre los documentos y diagramas.
También se detectó un error en la denominación del proceso central del DFD. Aunque "Sistema de Gestión Veterinaria" describía correctamente el dominio general, no respetaba la notación exigida por la cátedra. La corrección a "Gestionar Clínica Veterinaria" permitió adaptar el modelo a la convención enseñada.
En el modelo de dominio se revisaron especialmente las multiplicidades, ya que una propuesta generada automáticamente puede establecer relaciones que resultan razonables desde un punto de vista genérico, pero que no representan correctamente las reglas del dominio. La relación entre Mascota, HistoriaClinica y Consulta fue analizada y corregida de acuerdo con el funcionamiento que el grupo definió para el proyecto.


Dinámica de trabajo y reflexión final:

La dinámica de trabajo con IA fue, por lo tanto, iterativa y crítica. Como estudiantes se lideró el proceso aportando las consignas del TP, el material teórico de la materia, los borradores de archivos construidos por el grupo y además de los diagramas en desarrollo. La IA se utilizó para proponer estructuras, detectar posibles problemas y sugerir alternativas.
Posteriormente, las propuestas fueron revisadas por el grupo y contrastadas con la teoría oficial de la cátedra. Cuando una sugerencia era compatible con el proyecto y con los contenidos vistos, se aceptaba o adaptaba; cuando suponía un alcance excesivo, una decisión de dominio incorrecta o no respetaba una convención de la materia, se modificaba o descartaba.
Como resultado, el grupo no solo obtuvo una versión más consistente del SRS y de los demás artefactos del TP1, sino que también pudo identificar y justificar las decisiones tomadas durante el desarrollo del proyecto.

---

## Entrega TP2

Como fue solicitado en las normativas del trabajo, se deja documentado en el presente archivo los prompts utilizados para que la IA pueda generar respuestas de valor como así también las respuestas obtenida.

**Prompt utilizado para la primer iteración (generación del código):**
Actúa como un profesional de la Ingeniería de Software experto en UI/UX y Desarrollador Frontend Senior. Tu tarea es generar el maquetado de la interfaz de usuario para una Aplicación Web, cumpliendo estrictamente con los principios del diseño centrado en el usuario.
1. Contexto y Perfil de Usuario El sistema es una aplicación web de gestión. El actor principal y usuario final de estas pantallas es un Veterinario. Perfil del usuario: Es un profesional de la salud animal que utiliza el sistema durante las consultas clínicas. Su entorno de uso suele ser un consultorio, requiriendo eficiencia, rapidez y claridad visual, ya que tiene tiempo limitado entre pacientes.
2. Tarea y Flujo de Navegación Debes maquetar las pantallas correspondientes al flujo de navegación de los  escenarios de uso extraídos de nuestras historias de usuario definidos anteriormente.
3. Criterios Técnicos y Estéticos

Lenguaje y Framework: Exclusivamente HTML puro y CSS embebido o mediante clases utilitarias estándar. La estructura del HTML debe ser semántica y estar preparada para integrarse fácilmente con un entorno de desarrollo backend en Python (por ejemplo, lista para recibir variables de plantillas Jinja/Django).
Estética: Debe tener un diseño moderno, limpio y agradable. Utiliza una paleta de colores de clínica veterinaria (tonos que transmitan salud y calma, como blancos, grises claros, verdes agua o azules médicos).

Restricciones Críticas de Calidad El diseño de cada pantalla DEBE cumplir obligatoriamente con las 10 Heurísticas de Usabilidad de Nielsen. Debes prestar especial atención a:

Visibilidad del estado del sistema: Mostrar claramente en qué parte del flujo se encuentra el veterinario.
Prevención de errores: Evitar la carga de datos clínicos incorrectos.
Flexibilidad y eficiencia de uso: Accesos rápidos a las funciones más críticas de los 3 casos de uso.

Formato de Salida Genera el código HTML completo y funcional para las pantallas necesarias. Añade comentarios dentro del código HTML (usando <!-- -->) explicando brevemente cómo y dónde aplicaste heurísticas específicas de Nielsen en los componentes principales.

**Respuesta:**
Armé la Parte B en docs/ux/parte-b-diseno.md (secciones 4.1 a 4.3) y un maquetado navegable en docs/ux/maquetado-v1/, en Flask con HTML, con las cuatro pantallas de HU-01 a HU-03 y las 10 heurísticas de Nielsen aplicadas. No ejecuté ni probé el código. Para correrlo: pip install flask, luego python app.py y abrir http://127.0.0.1:5000. Para ver la alerta de HU-03, prescribí "Meloxicam" a Luna.

Como la consigna prohíbe pantallas sin historia del TP1, dejé afuera el gráfico de peso de CU-02, que no tiene ninguna historia asociada. El historial de CU-02 sí está, porque HU-02 lo necesita. Tampoco maqueté la consulta a OMIA, el fármaco vencido ni el login. Si querés incluir el gráfico, primero hay que escribir su historia en el TP1.

El perfil del veterinario se apoya en el TP1, salvo tres supuestos que declaré como del grupo y que conviene validar: dispositivo, urgencia y nivel técnico (S1 a S3). Los datos son ficticios; el perfil, la paleta y el flujo de pantallas los definí yo, así que revisalos antes de anotar en docs/uso-ia.md qué aceptaron o cambiaron. 


**Prompt utilizado para la segunda iteración:**
Actúa como un Especialista en Interfaz de Usuario (UI) y Usabilidad. Tu tarea es realizar una evaluación heurística rigurosa del código HTML adjunto, el cual corresponde a una pantalla de un sistema de gestión veterinaria.

1. Contexto de Evaluación

Perfil de Usuario: Veterinario. Profesional de la salud animal que usa el sistema en un consultorio, con tiempo limitado entre pacientes, requiriendo rapidez, claridad visual y prevención de errores clínicos.

Escenario de Uso: [INSTRUCCIÓN PARA EL GRUPO: Pegar aquí el escenario de uso específico de esta pantalla]

2. Tarea de Evaluación
Evalúa la interfaz proporcionada contrastándola contra las 10 Heurísticas de Usabilidad de Jakob Nielsen. Debes analizar la interfaz asumiendo la perspectiva del perfil de usuario definido, no de un usuario genérico.

3. Formato de Salida Obligatorio
Para CADA UNA de las 10 heurísticas, debes proveer el siguiente formato estructurado:

Heurística [Número y Nombre]

Estado: [Cumple / Cumple Parcialmente / Incumple]

Justificación: Explica detalladamente por qué, basándote en elementos concretos del código HTML y en el contexto del veterinario.

Hallazgo (si aplica): Si el estado es "Incumple" o "Cumple Parcialmente", describe exactamente qué elemento falla y cuál es el riesgo de usabilidad.

IMPORTANTE: En esta respuesta, NO generes código HTML para solucionar los problemas. Tu único objetivo es diagnosticar y auditar la interfaz. 


Actúa como un Desarrollador Frontend. Tras someter la interfaz de la pantalla anterior a una evaluación heurística, el equipo de desarrollo ha analizado tus hallazgos y ha decidido aceptar e implementar una serie de correcciones específicas para mejorar la usabilidad.

1. Tarea
Debes actualizar el código HTML original que te proporcioné anteriormente para solucionar ÚNICAMENTE los problemas detallados en la lista de hallazgos aceptados a continuación.

2. Hallazgos Aceptados a Corregir:
[INSTRUCCIÓN PARA EL GRUPO: Pegar aquí solo las heurísticas que el grupo decidió aceptar y que necesitan corrección]

3. Formato de Salida (Modo de Reemplazo)
No me devuelvas todo el código HTML completo de nuevo. Para cada corrección, entrégame el código de manera concreta indicando exactamente dónde implementar los cambios utilizando el siguiente formato estricto:

Corrección para Heurística [Número]
BUSCAR ESTE BLOQUE EN EL CÓDIGO ORIGINAL:

**Respuesta:**
Buenas tardes, Augusto. Revisé la consigna del TP2, el perfil de usuario, los RF/SRS y los cuatro maquetados reales del ZIP. La sección 4.4 pide evaluar **cada pantalla heurística por heurística**, considerando al usuario y escenario concreto; la 4.5 exige que ustedes después acepten o rechacen cada hallazgo y justifiquen esa decisión. 

Voy a separar claramente:

* **Evaluación crítica inicial:** lo que yo detecto.
* **Qué considero correcto, parcial o incumplido.**
* **Qué deberían discutir ustedes como grupo.**
* **Qué cambios recomiendo aceptar.**
* **Dónde hacerlos exactamente**, con bloques de reemplazo.
* **Cómo documentar cada decisión** en `docs/ui/heuristic-review/`.

> **Importante:** no recomiendo marcar "incumple" simplemente porque podría mejorarse. Para una defensa oral es mucho más sólido distinguir **cumple**, **cumple parcialmente** e **incumple** y justificar por qué.

---

# 1. Contexto que vamos a utilizar

Las cuatro pantallas son:

| Pantalla          | Historia | Escenario                                                         |
| ----------------- | -------- | ----------------------------------------------------------------- |
| `consulta.html`   | HU-01    | Registrar consulta con datos obligatorios incompletos/incorrectos |
| `historial.html`  | HU-02    | Consultar historial y seleccionar una entrada para editar         |
| `editar.html`     | HU-02    | Corregir una entrada propia                                       |
| `prescribir.html` | HU-03    | Prescribir un medicamento que genera una alerta de interacción    |

Esto coincide con el perfil del **Médico Veterinario**, cuyo objetivo es registrar/consultar información clínica, mantener actualizado el historial y gestionar tratamientos. Además, el propio perfil indica como criterios de diseño mostrar claramente el estado de las operaciones, usar terminología veterinaria, prevenir errores, mostrar errores comprensibles, permitir cancelar/corregir y mantener los datos relevantes del paciente visibles. 

---

# 2. Resultado general de las 40 evaluaciones

Primero te dejo la matriz completa para que tengan una visión rápida.

**C = Cumple**
**CP = Cumple parcialmente**
**I = Incumple**

| Heurística de Nielsen                          | Nueva consulta | Historial | Editar entrada | Prescribir |
| ---------------------------------------------- | :------------: | :-------: | :------------: | :--------: |
| 1. Visibilidad del estado                      |       CP       |     C     |       CP       |    **I**   |
| 2. Correspondencia sistema-mundo real          |        C       |     C     |        C       |      C     |
| 3. Control y libertad del usuario              |        C       |     C     |        C       |    **I**   |
| 4. Consistencia y estándares                   |        C       |     C     |        C       |     CP     |
| 5. Prevención de errores                       |       CP       |     C     |       CP       |    **I**   |
| 6. Reconocimiento antes que recuerdo           |        C       |     C     |        C       |     CP     |
| 7. Flexibilidad y eficiencia                   |        C       |     CP    |        C       |     CP     |
| 8. Diseño estético/minimalista                 |        C       |     CP    |        C       |     CP     |
| 9. Ayuda para reconocer/recuperarse de errores |      **C**     |     C     |       CP       |    **I**   |
| 10. Ayuda y documentación                      |        C       |     CP    |        C       |     CP     |

Hay un punto que quiero remarcar desde ya:

## El problema más grave está en `prescribir.html`

No es solamente una mejora de UX.

El bloque:

```html
{% if alerta %}
  <div class="drug-interaction-card" ...>
      ...
      <textarea ...></textarea>

      <button ... type="submit">Continuar...</button>
      <button ... type="submit">Cancelar...</button>
  </div>
{% endif %}

<form method="post" ...>
```

está estructurado de manera que **la alerta y sus botones están fuera del formulario**.

Por lo tanto, los botones `type="submit"` no están asociados al `<form>` que procesa `/prescribir`.

Esto afecta directamente a:

* H3 — Control y libertad.
* H5 — Prevención de errores.
* H9 — Recuperación ante errores.
* H1 — Visibilidad/estado, porque se presenta una alerta que aparenta ofrecer acciones funcionales.

Este hallazgo sí lo considero un **incumplimiento real**, no una preferencia estética.

---

# 3. PANTALLA 1 — Nueva Consulta

Archivo:

```text
docs/ui/mockups/templates/consulta.html
```

---

## H1 — Visibilidad del estado del sistema

### Evaluación: **CUMPLE PARCIALMENTE**

La pantalla muestra correctamente el estado después de una operación:

```html
<div class="alert-banner err" role="alert">
```

para errores y mediante `flash()` después de guardar correctamente.

Además, cuando hay errores se informa:

> "No se pudo guardar la consulta"

y se conserva la información introducida.

El problema es que la interfaz **no tiene un estado explícito mientras se procesa el guardado**.

Para este mockup no considero que esto sea un incumplimiento grave porque no existe una operación asíncrona real. Sin embargo, desde la heurística 1, podría mejorarse el feedback del botón.

### Decisión que propondría

**Aceptar parcialmente**, no tratarlo como un defecto crítico.

No modificaría el código por este punto solamente.

---

# H2 — Correspondencia entre sistema y mundo real

### Evaluación: **CUMPLE**

Está muy bien resuelta.

La pantalla utiliza términos que corresponden directamente al trabajo veterinario:

* Fecha de Atención
* Peso Actual
* Síntomas
* Diagnóstico Preliminar
* Observaciones Clínicas
* Vacuna
* Patologías
* Procedimientos

No aparecen términos técnicos de programación ni nombres internos del sistema.

Además, el perfil establece explícitamente que se debe utilizar terminología relacionada con la gestión clínica veterinaria.

### Decisión

**Aceptar: cumple.**

No cambiaría nada.

---

# H3 — Control y libertad del usuario

### Evaluación: **CUMPLE**

Existe:

```html
<button class="btn" type="submit">Guardar Consulta</button>
<a class="btn btn-ghost" ...>Cancelar</a>
```

El veterinario puede:

1. cargar información;
2. guardar;
3. cancelar y volver al historial.

Además, el script global detecta modificaciones no guardadas:

```javascript
window.addEventListener('beforeunload', ...)
```

Esto es positivo porque evita perder accidentalmente información.

### Decisión

**Cumple.**

---

# H4 — Consistencia y estándares

### Evaluación: **CUMPLE**

Los elementos siguen los patrones visuales del resto:

* mismos botones;
* mismos campos;
* mismas tarjetas;
* mismo breadcrumb;
* mismo encabezado;
* misma información del paciente.

La pantalla utiliza además `label` asociados correctamente mediante `for`/`id`.

### Decisión

**Cumple.**

---

# H5 — Prevención de errores

### Evaluación: **CUMPLE PARCIALMENTE**

Hay bastante prevención:

```python
if not v.get("fecha"):
```

```python
elif v["fecha"] > date.today().isoformat():
```

```python
if peso <= 0:
```

y los errores se muestran individualmente.

Pero la prevención ocurre principalmente **después de enviar el formulario**.

Además, `_campos.html` no marca como `required` los campos obligatorios.

Por ejemplo:

```html
<input ...>
```

en lugar de:

```html
<input ... required>
```

La aplicación puede detectar el error, pero el navegador no ayuda a prevenirlo antes del envío.

### Decisión

Yo **aceptaría el hallazgo**.

---

# H6 — Reconocimiento antes que recuerdo

### Evaluación: **CUMPLE**

Los campos están explícitamente etiquetados.

Por ejemplo:

```html
<label for="peso" ...>
```

y además hay ayudas:

> Ejemplo: 6.8

> Describí detalladamente los signos clínicos

> Diagnóstico de trabajo o hipótesis principal

El usuario no tiene que recordar qué debe introducir.

### Decisión

**Cumple.**

---

# H7 — Flexibilidad y eficiencia de uso

### Evaluación: **CUMPLE**

La pantalla tiene:

* estructura en dos/tres columnas;
* atajo `Ctrl + Enter`;
* datos del paciente visibles;
* navegación por breadcrumb;
* campos agrupados.

Para un veterinario que realiza repetidamente consultas, esto reduce pasos.

### Decisión

**Cumple.**

---

# H8 — Diseño estético y minimalista

### Evaluación: **CUMPLE**

La información está agrupada:

```html
<fieldset>
```

en:

> Datos Clínicos Obligatorios

y:

> Vacunas y Prestaciones Complementarias

Esto es especialmente apropiado porque el formulario tiene varios campos.

No se agregan elementos decorativos irrelevantes.

### Decisión

**Cumple.**

---

# H9 — Ayudar a reconocer, diagnosticar y recuperarse de errores

### Evaluación: **CUMPLE**

Esta es una de las partes mejor resueltas.

El sistema indica:

```html
No se pudo guardar la consulta
```

muestra cantidad de errores y además genera enlaces:

```html
<a href="#{{ k }}">
```

que llevan al campo correspondiente.

También conserva lo que el usuario había escrito.

Esto coincide directamente con RF-11, que exige informar el campo y motivo del error. 

### Decisión

**Cumple.**

---

# H10 — Ayuda y documentación

### Evaluación: **CUMPLE**

No existe un manual enorme, pero la pantalla proporciona ayuda contextual suficiente mediante:

```html
<span class="field-help">
```

Por ejemplo:

> Ejemplo: 6.8

y:

> Diagnóstico de trabajo o hipótesis principal.

Para esta tarea no hace falta una documentación adicional.

### Decisión

**Cumple.**

---

# 4. Cambio recomendado en Nueva Consulta

El único cambio que recomiendo aceptar es H5.

## Archivo

```text
docs/ui/mockups/templates/_campos.html
```

### Actualmente

```html
{% if tipo == 'area' %}
  <textarea id="{{ k }}" name="{{ k }}" rows="3" class="field-control {{ 'invalid' if errores.get(k) }}">{{ v.get(k, '') }}</textarea>
{% else %}
  <input id="{{ k }}" name="{{ k }}" type="{{ tipo }}" value="{{ v.get(k, '') }}" class="field-control {{ 'invalid' if errores.get(k) }}"
         {% if tipo == 'number' %} step="0.1" inputmode="decimal" {% endif %}
         {% if k in ('fecha', 'vigencia') %} {{ 'max' if k == 'fecha' else 'min' }}="{{ hoy }}" {% endif %}>
{% endif %}
```

### Reemplazar por

```html
{% if tipo == 'area' %}
  <textarea
    id="{{ k }}"
    name="{{ k }}"
    rows="3"
    class="field-control {{ 'invalid' if errores.get(k) }}"
    {% if '*' in label %}required{% endif %}
  >{{ v.get(k, '') }}</textarea>
{% else %}
  <input
    id="{{ k }}"
    name="{{ k }}"
    type="{{ tipo }}"
    value="{{ v.get(k, '') }}"
    class="field-control {{ 'invalid' if errores.get(k) }}"
    {% if '*' in label %}required{% endif %}
    {% if tipo == 'number' %}
      step="0.1"
      min="0.1"
      inputmode="decimal"
    {% endif %}
    {% if k in ('fecha', 'vigencia') %}
      {{ 'max' if k == 'fecha' else 'min' }}="{{ hoy }}"
    {% endif %}
  >
{% endif %}
```

Esto hace que el navegador también contribuya a prevenir:

* campos obligatorios vacíos;
* pesos no positivos.

El servidor sigue siendo responsable de la validación definitiva.

---

# 5. PANTALLA 2 — Historial Clínico

Archivo:

```text
docs/ui/mockups/templates/historial.html
```

---

# H1 — Visibilidad del estado

### **CUMPLE**

La pantalla deja muy claro:

* paciente actual;
* historial;
* orden cronológico;
* peso;
* autor;
* si una entrada fue modificada;
* si se puede editar.

Además, cuando se realiza una modificación aparece un `flash` de confirmación.

---

# H2 — Correspondencia con mundo real

### **CUMPLE**

La representación:

```text
Fecha
Autor
Peso
Síntomas
Diagnóstico
Observaciones
```

corresponde directamente a una historia clínica veterinaria.

La frase:

> Historial Clínico Cronológico

es perfectamente comprensible para el usuario.

---

# H3 — Control y libertad

### **CUMPLE**

Desde el historial se puede:

* crear consulta;
* prescribir;
* editar una entrada propia;
* volver mediante breadcrumbs.

Y cuando una entrada no puede editarse, la interfaz explica:

> Solo su autor/a puede editar esta entrada (RF-08)

Eso es particularmente bueno porque evita que una acción no disponible parezca un error.

---

# H4 — Consistencia

### **CUMPLE**

Utiliza el mismo:

* navbar;
* paciente;
* breadcrumb;
* sistema de botones;
* tarjetas;
* tipografía;
* colores.

---

# H5 — Prevención de errores

### **CUMPLE**

La propia interfaz evita ofrecer "Editar" para una entrada que pertenece a otro profesional:

```jinja
{% if e.autor == vet %}
```

Esto es una buena aplicación de prevención.

No solamente se informa el problema: se evita presentar una acción que el usuario no puede ejecutar.

---

# H6 — Reconocimiento antes que recuerdo

### **CUMPLE**

Toda la información relevante está visible en la propia pantalla.

El veterinario no tiene que recordar:

* qué paciente está viendo;
* quién creó la entrada;
* qué peso tenía;
* qué diagnóstico se registró;
* si la entrada fue modificada.

---

# H7 — Flexibilidad y eficiencia

### **CUMPLE PARCIALMENTE**

La pantalla permite acceder rápidamente a:

```text
Nueva Consulta
Prescribir Medicación
Editar esta Entrada
```

Sin embargo, cuando el historial crezca considerablemente, esta vista puede volverse larga y poco eficiente.

Pero esto **no está demostrado como problema en el mockup actual**, porque el escenario trabajado no especifica historiales masivos.

### Decisión

Yo lo dejaría como **parcial**, pero **no implementaría un buscador/filtro nuevo**, porque eso estaría agregando funcionalidad no solicitada por la historia.

Esto es importante para la defensa: el TP2 dice que no deben agregar historias nuevas ni pantallas no respaldadas por TP1. 

---

# H8 — Diseño estético/minimalista

### **CUMPLE PARCIALMENTE**

La información es necesaria, pero cada entrada muestra bastantes datos simultáneamente.

Sin embargo, el uso de:

```html
<details>
```

para la explicación de RF-08 es una buena decisión porque permite ocultar información secundaria.

Por eso no lo considero incumplimiento.

### Decisión

**Parcial**, sin cambio obligatorio.

---

# H9 — Recuperación ante errores

### **CUMPLE**

Si el usuario intenta editar una entrada que no corresponde:

```python
flash("Solo el profesional autor de la entrada puede editarla...")
```

y vuelve al historial.

Además, el historial muestra quién puede editar.

---

# H10 — Ayuda/documentación

### **CUMPLE PARCIALMENTE**

Existe ayuda contextual:

```html
<details>
```

que explica RF-08.

Pero no existe ayuda para conceptos como:

* qué significa "Modificada";
* qué representa cada dato;
* qué hacer si existe una inconsistencia.

No lo considero un incumplimiento porque el escenario no requiere un sistema de ayuda completo.

### Decisión

**Parcial, sin cambio obligatorio.**

---

# 6. PANTALLA 3 — Editar Entrada

Archivo:

```text
docs/ui/mockups/templates/editar.html
```

---

# H1 — Visibilidad del estado

### **CUMPLE PARCIALMENTE**

La pantalla informa claramente:

> Editar Entrada Clínica del...

y:

> Trazabilidad Profesional (RF-08)

Además, después de guardar aparece:

> Entrada actualizada correctamente.

Pero el error de validación actual:

```html
<div class="alert-banner err" role="alert">
```

solo muestra el texto del error.

No existe un resumen tan claro como en Nueva Consulta.

### Decisión

**Parcial.**

Yo sí aceptaría una pequeña mejora.

---

# H2 — Correspondencia con mundo real

### **CUMPLE**

La pantalla diferencia:

> Datos Históricos Inmutables

de:

> Observaciones Clínicas (Corrección / Rectificación)

Eso refleja muy bien la operación real.

---

# H3 — Control y libertad

### **CUMPLE**

Tiene:

```html
Confirmar Cambios
Cancelar
```

y el usuario puede regresar al historial.

---

# H4 — Consistencia

### **CUMPLE**

Visualmente mantiene el mismo sistema.

---

# H5 — Prevención de errores

### **CUMPLE PARCIALMENTE**

El servidor impide dejar la observación vacía:

```python
if not obs:
    err["obs"] = "La observación no puede quedar vacía."
```

Pero el textarea no tiene:

```html
required
```

Por lo tanto, nuevamente la prevención podría comenzar antes del envío.

---

# H6 — Reconocimiento antes que recuerdo

### **CUMPLE**

Se muestran inmediatamente:

* fecha;
* autor;
* peso;
* síntomas;
* diagnóstico.

El veterinario puede decidir qué modificar sin tener que recordar la entrada original.

---

# H7 — Flexibilidad y eficiencia

### **CUMPLE**

La pantalla permite corregir directamente la observación.

No obliga a reconstruir la consulta completa.

Esto es especialmente adecuado porque RF-08 habla específicamente de editar/corregir entradas previas. 

---

# H8 — Diseño minimalista

### **CUMPLE**

La pantalla tiene una sola operación principal:

> corregir observaciones.

Los datos históricos están separados visualmente de los editables.

---

# H9 — Recuperación ante errores

### **CUMPLE PARCIALMENTE**

El usuario recibe:

> La observación no puede quedar vacía.

y el valor introducido se conserva.

Pero el mensaje no está asociado semánticamente al campo mediante `aria-describedby` y tampoco ofrece un enlace directo al campo.

Esto es mejorable.

---

# H10 — Ayuda/documentación

### **CUMPLE**

La explicación:

> Trazabilidad Profesional (RF-08)...

ayuda al usuario a comprender qué sucederá después de confirmar.

---

# 7. Cambios recomendados en Editar

## Cambio 1 — `required` + asociación del error

### Actualmente

```html
<textarea id="obs" name="obs" rows="5" class="field-control {{ 'invalid' if errores }}" aria-required="true">{{ obs }}</textarea>
```

### Reemplazar por

```html
<textarea
  id="obs"
  name="obs"
  rows="5"
  class="field-control {{ 'invalid' if errores }}"
  aria-required="true"
  {% if errores.obs %}aria-describedby="obs-error"{% endif %}
  required
>{{ obs }}</textarea>
```

Y actualmente:

```html
{% if errores.obs %}<span class="field-error"> {{ errores.obs }}</span>{% endif %}
```

### Reemplazar por

```html
{% if errores.obs %}
  <span class="field-error" id="obs-error" role="alert">
    {{ errores.obs }}
  </span>
{% endif %}
```

Esto mejora H5 y H9.

---

# Cambio 2 — hacer que el error sea navegable

Actualmente:

```html
{% if errores %}
  <div class="alert-banner err" role="alert"> {{ errores.obs }}</div>
{% endif %}
```

### Reemplazar por

```html
{% if errores %}
  <div class="alert-banner err" role="alert" tabindex="-1" id="error-summary">
    <div>
      <strong>No se pudo actualizar la entrada.</strong>
      <p style="font-size:0.875rem; margin-top:0.25rem;">
        Revisá el siguiente campo antes de confirmar:
      </p>
      <a href="#obs" style="color:#b91c1c; text-decoration:underline;">
        {{ errores.obs }}
      </a>
    </div>
  </div>
{% endif %}
```

Así queda alineado con la excelente estrategia que ya utilizaron en `consulta.html`.

---

# 8. PANTALLA 4 — Prescribir Medicación

Esta es la que necesita más atención.

Archivo:

```text
docs/ui/mockups/templates/prescribir.html
```

---

# H1 — Visibilidad del estado

### **INCUMPLE**

Cuando se detecta la interacción se muestra:

> ALERTA CRÍTICA: Incompatibilidad Medicamentosa Detectada

Eso está bien.

Pero la interfaz presenta una situación interactiva sin garantizar que las acciones asociadas funcionen.

Además, no queda visualmente suficientemente claro si:

* la prescripción fue cancelada;
* quedó pendiente;
* se requiere justificación;
* se puede continuar.

La intención está escrita, pero la interacción está mal conectada.

### Decisión

**Aceptar como incumplimiento.**

---

# H2 — Correspondencia con mundo real

### **CUMPLE**

Los términos son adecuados:

* Medicación;
* Suplementación;
* Dosis;
* Intervalo;
* Indicaciones;
* Posología;
* Interacción medicamentosa;
* Justificación clínica.

Muy buen cumplimiento.

---

# H3 — Control y libertad del usuario

### **INCUMPLE**

Este es uno de los problemas principales.

La interfaz presenta:

```html
<button ...>Continuar Bajo Mi Responsabilidad Profesional</button>
<button ...>Cancelar Prescripción</button>
```

pero están fuera del `<form>`.

Por lo tanto, el usuario percibe que puede decidir, pero la estructura HTML no garantiza que esas acciones ejecuten el flujo previsto.

Esto contradice directamente la necesidad del escenario de HU-03:

> el sistema debe informar la interacción y solicitar una decisión al veterinario.

### Decisión

**Aceptar el hallazgo.**

---

# H4 — Consistencia y estándares

### **CUMPLE PARCIALMENTE**

Visualmente sigue el sistema.

Pero hay una inconsistencia importante:

En las otras pantallas, los controles de la operación están contenidos dentro del formulario correspondiente.

En esta pantalla, la alerta tiene controles de formulario separados del formulario.

### Decisión

**Parcial**, derivada del mismo problema estructural.

---

# H5 — Prevención de errores

### **INCUMPLE**

Esta pantalla debería ser justamente la que más prevención proporcione.

El flujo correcto es:

```text
Intentar prescribir
        ↓
Detectar interacción
        ↓
Advertir
        ↓
Solicitar justificación
        ↓
Cancelar o continuar
```

Actualmente la interfaz visualiza ese flujo, pero los controles de la alerta no están correctamente asociados al formulario.

Además, la justificación no tiene:

```html
required
```

y la única validación efectiva es del servidor.

### Decisión

**Aceptar.**

---

# H6 — Reconocimiento antes que recuerdo

### **CUMPLE PARCIALMENTE**

La alerta informa explícitamente:

```html
Conflicto detectado con el tratamiento activo
```

y muestra el medicamento conflictivo y el efecto adverso.

Eso está muy bien.

Pero el usuario debe interpretar por sí mismo qué hacer con la alerta.

Podemos mejorar esto haciendo explícita la secuencia:

> Para continuar, escribí una justificación clínica y seleccioná "Continuar".

### Decisión

**Parcial.**

---

# H7 — Flexibilidad y eficiencia

### **CUMPLE PARCIALMENTE**

Hay un buen diseño porque no obliga al veterinario a abandonar el flujo.

Puede:

* cancelar;
* justificar y continuar.

Pero el flujo actual tiene el problema estructural de los botones.

Una vez corregido, esta heurística pasaría a **cumple**.

---

# H8 — Diseño estético y minimalista

### **CUMPLE PARCIALMENTE**

La alerta es deliberadamente prominente y eso está justificado porque se trata de un riesgo clínico.

Pero hay bastante información:

* tratamiento activo;
* tipo;
* fármaco;
* dosis;
* indicaciones;
* vigencia;
* alerta;
* justificación;
* acciones.

No es necesariamente incorrecto, pero la alerta podría jerarquizar mejor qué debe leer primero.

### Decisión

**Parcial, sin necesidad de un cambio estructural adicional.**

---

# H9 — Recuperación ante errores

### **INCUMPLE**

La interacción medicamentosa constituye precisamente una condición en la que el sistema debe ayudar al usuario a recuperarse de una acción potencialmente peligrosa.

La interfaz tiene la información necesaria, pero la interacción de los botones está mal implementada.

Además, cuando la justificación es inválida:

```html
{% if errores.get('justificacion') %}
```

el mensaje no tiene `id` ni relación explícita con el textarea.

### Decisión

**Aceptar.**

---

# H10 — Ayuda y documentación

### **CUMPLE PARCIALMENTE**

Hay bastante ayuda contextual mediante:

```html
placeholder="Ejemplo: ..."
```

y la explicación del conflicto.

Pero sería conveniente que la propia alerta explicara brevemente:

> Para continuar bajo responsabilidad profesional se requiere una justificación clínica.

### Decisión

**Parcial.**

---

# 9. CORRECCIÓN IMPORTANTE DE `prescribir.html`

Acá sí recomiendo modificar el código.

La solución más limpia es que **la alerta forme parte del mismo formulario**.

Actualmente tienen:

```html
{% if alerta %}
  <div class="drug-interaction-card" ...>
      ...
  </div>
{% endif %}

<form method="post" class="editable surface-card" novalidate>
```

## Hay que cambiar el orden.

### Reemplazar desde:

```html
{% if alerta %}
```

hasta:

```html
{% endif %}

<form method="post" class="editable surface-card" novalidate>
```

por:

```html
<form method="post" class="editable surface-card" novalidate id="prescripcion-form">

  {% if alerta %}
    <div class="drug-interaction-card" role="alert" aria-labelledby="alert-title">
      <div id="alert-title" class="interaction-header">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
          <line x1="12" y1="9" x2="12" y2="13"/>
          <line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        <span>ALERTA CRÍTICA: Incompatibilidad Medicamentosa Detectada</span>
      </div>

      <div class="interaction-body">
        <p style="font-size:0.95rem; font-weight:700; color:#9a3412; margin-bottom:0.35rem;">
          Conflicto detectado con el tratamiento activo:
          <mark style="background:#fed7aa; padding:0.1rem 0.5rem; border-radius:4px; font-weight:800; color:#7c2d12;">
            {{ alerta[0] }}
          </mark>
        </p>

        <p style="font-size:0.875rem; color:#c2410c; line-height:1.5;">
          <strong>Efecto clínico adverso:</strong> {{ alerta[1] }}
        </p>
      </div>

      <div class="form-field" style="margin-bottom:1.25rem;">
        <label for="justificacion" class="field-label" style="color:#7c2d12; font-weight:700;">
          Justificación Clínica Profesional (Requerida para autorizar):
        </label>

        <textarea
          id="justificacion"
          name="justificacion"
          rows="3"
          class="field-control {{ 'invalid' if errores.get('justificacion') }}"
          aria-required="true"
          {% if errores.get('justificacion') %}aria-describedby="justificacion-error"{% endif %}
          required
          placeholder="Escribí la razón clínica por la cual considerás necesario prescribir este fármaco a pesar del riesgo..."
        >{{ v.get('justificacion', '') }}</textarea>

        {% if errores.get('justificacion') %}
          <span class="field-error" id="justificacion-error" role="alert">
            {{ errores.justificacion }}
          </span>
        {% endif %}
      </div>

      <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
        <button
          class="btn btn-danger"
          name="accion"
          value="continuar"
          type="submit"
        >
          Continuar Bajo Mi Responsabilidad Profesional
        </button>

        <button
          class="btn btn-sec"
          name="accion"
          value="cancelar"
          type="submit"
          formnovalidate
        >
          Cancelar Prescripción
        </button>
      </div>
    </div>
  {% endif %}
```

Y después **mantener el resto del formulario**, empezando por:

```html
<div class="form-field">
  <label for="tipo" class="field-label">Tipo de Prescripción</label>
```

Es decir, ahora todo queda dentro de:

```html
<form ... id="prescripcion-form">
```

y el:

```html
</form>
```

final sigue siendo el mismo.

---

# 10. Corrección adicional en Prescribir: no usar `alertdialog`

Actualmente tienen:

```html
role="alertdialog"
```

pero no es realmente un diálogo modal.

No hay:

* modal;
* bloqueo del fondo;
* gestión de foco;
* botón de cierre propio de diálogo.

Por lo tanto, es más correcto utilizar:

```html
role="alert"
```

como puse en el reemplazo.

### Documentación

Esto lo pueden justificar así:

> **Hallazgo aceptado — H1/H3/H5/H9:** la alerta se presentaba con controles interactivos fuera del formulario principal y con un rol ARIA de diálogo que no correspondía con la interacción implementada. Se modificó la estructura para integrar la alerta dentro del formulario y permitir que las acciones de continuar/cancelar sean operables. También se reemplazó `role="alertdialog"` por `role="alert"` porque la interfaz no implementa un diálogo modal.

Eso es una **muy buena decisión para defender oralmente**.

---

# 11. Corrección del `required` en Prescribir

Como `_campos.html` ahora puede detectar `*`, estos:

```html
{{ campo('farmaco', 'Fármaco o Suplemento *', 'text', ...) }}
{{ campo('dosis', 'Dosis e Intervalo *', 'text', ...) }}
```

pasarán a generar automáticamente:

```html
required
```

con la modificación que vimos antes.

Esto resuelve parcialmente H5.

---

# 12. Un pequeño cambio en el footer

Hay otro detalle que considero importante.

En `base.html` aparece:

```html
Atajo de teclado: Presioná <strong>Ctrl + Enter</strong> en cualquier formulario para guardar automáticamente.
```

La palabra **"automáticamente"** puede ser confusa.

El atajo realmente hace:

```javascript
form.requestSubmit();
```

Es decir, **envía el formulario**. No guarda mágicamente sin pasar por el proceso normal.

### Recomiendo reemplazar:

```html
<p style="margin-top:0.25rem;"><small> Atajo de teclado: Presioná <strong>Ctrl + Enter</strong> en cualquier formulario para guardar automáticamente.</small></p>
```

por:

```html
<p style="margin-top:0.25rem;">
  <small>
    Atajo de teclado: presioná <strong>Ctrl + Enter</strong> dentro de un formulario para enviarlo.
  </small>
</p>
```

### ¿Por qué?

Porque es más fiel al comportamiento real y evita una falsa expectativa.

Esto es una mejora de:

* H1 — visibilidad;
* H6 — reconocimiento;
* H5 — prevención de errores.

No lo considero un incumplimiento grave, pero sí lo cambiaría.

---

# 13. Una mejora de accesibilidad en la búsqueda global

Esto afecta a las cuatro pantallas porque está en `base.html`.

Actualmente:

```html
<input id="q" name="q" list="patient-list" placeholder="Buscar paciente por nombre..." autocomplete="off">
```

Solo tenemos `placeholder`.

El placeholder **no debería reemplazar una etiqueta**.

### Reemplazar:

```html
<form class="search-bar" action="{{ url_for('buscar') }}" method="GET" role="search">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
  <input id="q" name="q" list="patient-list" placeholder="Buscar paciente por nombre..." autocomplete="off">
```

por:

```html
<form class="search-bar" action="{{ url_for('buscar') }}" method="GET" role="search">
  <label for="q" class="sr-only">Buscar paciente por nombre</label>

  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
    <circle cx="11" cy="11" r="8"/>
    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
  </svg>

  <input
    id="q"
    name="q"
    list="patient-list"
    placeholder="Buscar paciente por nombre..."
    autocomplete="off"
  >
```

Y en `style.css`, agregar:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

No es necesario presentarlo como un gran defecto de las cuatro pantallas. Lo documentaría como **mejora transversal de accesibilidad**.

---

# 14. ¿Qué NO cambiaría?

Esto también es importante.

No cambiaría estas cosas simplemente porque "podrían ser mejores":

### No agregaría filtros al historial

Porque no forman parte de HU-02.

### No agregaría gráficos

Aunque RF-12 menciona gráficos/reportes, las cuatro pantallas analizadas no corresponden a esa HU.

### No agregaría nuevas pantallas

La consigna explícitamente limita el maquetado a historias del TP1. 

### No agregaría confirmaciones innecesarias

Por ejemplo:

> "¿Seguro que desea cancelar?"

en cada botón.

En el escenario de trabajo del veterinario eso puede aumentar fricción sin aportar suficiente valor.

### No modificaría la estética general

El sistema ya mantiene una identidad visual consistente.

---

# 15. Cómo documentar esto en los cuatro Markdown

La consigna exige que **cada pantalla tenga su propio documento** en:

```text
docs/ui/heuristic-review/
```

y que contenga los prompts, respuesta completa de IA, justificación del grupo y ciclos adicionales. 

Los cuatro archivos que ya existen son:

```text
hu01-nueva-consulta.md
hu02-historial.md
hu02-editar.md
hu03-prescripcion.md
```

pero en el ZIP están **vacíos**, así que actualmente esa parte de la documentación todavía no está realizada.

---

# 16. Estructura concreta que les recomiendo para cada archivo

No pondría simplemente:

> H1: cumple
> H2: cumple
> etc.

Eso queda demasiado pobre para la defensa.

Usaría:

```markdown
# Evaluación heurística — HU-01 Nueva Consulta

## 1. Pantalla evaluada

- Historia de usuario: HU-01
- Pantalla: Nueva Consulta
- Actor: Médico Veterinario
- Escenario: Datos obligatorios incompletos o con formato inválido

## 2. Prompt utilizado

[PEGAR ACÁ EL PROMPT EXACTO UTILIZADO]

## 3. Respuesta de la IA

[PEGAR ACÁ LA RESPUESTA COMPLETA DE LA IA]

## 4. Revisión crítica del grupo

### H1 — Visibilidad del estado del sistema

**Resultado de la IA:** ...

**Decisión del grupo:** Aceptado / Rechazado

**Justificación:**

...

### H2 — Correspondencia entre el sistema y el mundo real

**Resultado de la IA:** ...

**Decisión del grupo:** Aceptado / Rechazado

**Justificación:**

...

[HASTA H10]

## 5. Cambios aceptados

### Cambio 1 — ...

**Heurística:** H5

**Problema detectado:**

...

**Archivo:**

`docs/ui/mockups/templates/_campos.html`

**Cambio realizado:**

...

## 6. Ciclo adicional

**Prompt:**

...

**Resultado:**

...

**Decisión del grupo:**

...

```

---

# 17. Cómo deberían redactar la revisión crítica

Acá está probablemente lo más importante del TP.

No tienen que decir:

> "La IA dijo que H5 no cumple, entonces cambiamos H5."

La consigna dice explícitamente que la IA identifica posibles problemas, pero **el criterio sobre su validez corresponde al grupo**. 

Por ejemplo, para Historial/H7:

> **Decisión: rechazado.**
>
> La IA considera que la ausencia de filtros dificulta la eficiencia en historiales extensos. El grupo rechaza el hallazgo porque el escenario de uso definido para HU-02 consiste en consultar una entrada previa y editarla, y el TP1 no especifica filtros o búsquedas dentro del historial. Incorporar esta funcionalidad implicaría ampliar el alcance de la interfaz más allá de las historias trabajadas.

Eso es **muchísimo mejor** que:

> "No estamos de acuerdo porque nos parece que está bien."

---

# 18. Ejemplo de aceptación de un hallazgo

Para `prescribir.html`:

> **Decisión: aceptado.**
>
> Se acepta el hallazgo porque la alerta de interacción medicamentosa presenta acciones de continuar y cancelar que, en la implementación original, se encuentran fuera del formulario que procesa la solicitud. Esto afecta directamente la capacidad del veterinario para controlar la operación y recuperarse de una situación de riesgo. Se modifica la estructura para integrar la alerta y sus controles dentro del formulario de prescripción.

Esto conecta directamente:

```text
heurística
      ↓
problema concreto
      ↓
usuario
      ↓
escenario
      ↓
cambio
```

Eso es exactamente lo que les interesa demostrar.

---

# 19. Resumen de cambios que recomiendo implementar

Yo haría **estos cambios y no más**:

### Cambio 1 — `_campos.html`

Agregar:

```html
required
```

a campos marcados con `*` y:

```html
min="0.1"
```

para peso.

**Heurísticas:** H5.

---

### Cambio 2 — `editar.html`

Agregar:

```html
required
```

y:

```html
aria-describedby="obs-error"
```

al campo `obs`.

Crear:

```html
id="obs-error"
```

en el mensaje.

**Heurísticas:** H5, H9.

---

### Cambio 3 — `editar.html`

Convertir el error general en un resumen navegable hacia:

```html
#obs
```

**Heurísticas:** H1, H9.

---

### Cambio 4 — `prescribir.html`

Mover la alerta **dentro del formulario**.

**Heurísticas:** H1, H3, H4, H5, H9.

Este es el cambio más importante.

---

### Cambio 5 — `prescribir.html`

Cambiar:

```html
role="alertdialog"
```

por:

```html
role="alert"
```

porque no es realmente un diálogo modal.

**Heurísticas:** H1, H4, H6.

---

### Cambio 6 — `prescribir.html`

Hacer `justificacion`:

```html
required
```

y asociar su mensaje:

```html
aria-describedby="justificacion-error"
```

**Heurísticas:** H5, H9.

---

### Cambio 7 — `base.html`

Cambiar el texto:

```text
guardar automáticamente
```

por:

```text
enviarlo
```

**Heurísticas:** H1, H6.

---

### Cambio 8 — `base.html`

Agregar `label` accesible al buscador.

**Heurísticas:** H6, H10.

---

# 20. Resultado esperado después de los cambios

La matriz debería quedar aproximadamente así:

| Heurística        | Nueva Consulta | Historial | Editar | Prescribir |
| ----------------- | :------------: | :-------: | :----: | :--------: |
| H1 Estado         |       CP       |     C     |    C   |    **C**   |
| H2 Mundo real     |        C       |     C     |    C   |      C     |
| H3 Control        |        C       |     C     |    C   |    **C**   |
| H4 Consistencia   |        C       |     C     |    C   |      C     |
| H5 Prevención     |      **C**     |     C     |  **C** |    **C**   |
| H6 Reconocimiento |        C       |     C     |    C   |      C     |
| H7 Flexibilidad   |        C       |     CP    |    C   |      C     |
| H8 Minimalismo    |        C       |     CP    |    C   |     CP     |
| H9 Recuperación   |        C       |     C     |  **C** |    **C**   |
| H10 Ayuda         |        C       |     CP    |    C   |     CP     |

Y eso me parece un resultado **mucho más defendible académicamente** que intentar conseguir artificialmente diez "cumple" en cada pantalla.

---

## Conclusión crítica

La primera iteración **no está mal hecha**. De hecho, tiene varias decisiones bastante buenas: labels, breadcrumbs, conservación de datos después de errores, mensajes específicos, información persistente del paciente, separación entre datos históricos y editables, y una alerta clínica visualmente priorizada.

El problema más serio está concentrado en **Prescribir Medicación**, donde la implementación visual de la alerta y su implementación HTML no coinciden. La interfaz dice "podés continuar/cancelar", pero la estructura del formulario no respalda correctamente esas acciones. Ese es exactamente el tipo de problema que vale la pena detectar mediante las heurísticas.

Además, la evaluación debe quedar como **primer análisis crítico**, no como verdad definitiva: ustedes tienen que revisar cada uno de estos 40 resultados y decidir **aceptar/rechazar**, tal como exige la sección 4.5. 

Y para la entrega, recuerden que los cuatro documentos de `heuristic-review` deben contener no solamente esta evaluación, sino también **el prompt usado, la respuesta completa de la IA, la decisión del grupo para cada hallazgo y los ciclos adicionales de modificación**. 
