## H1 — Visibilidad del estado
**Evaluación IA:** CUMPLE
**Justificación IA:** La pantalla deja muy claro:

paciente actual;
historial;
orden cronológico;
peso;
autor;
si una entrada fue modificada;
si se puede editar.

Además, cuando se realiza una modificación aparece un flash de confirmación.

**Decisión del Grupo:** DE ACUERDO


## H2 — Correspondencia con mundo real
**Evaluación IA:** CUMPLE
**Justificación IA:** La representación corresponde directamente a una historia clínica veterinaria.
**Decisión del Grupo:** DE ACUERDO


## H3 — Control y libertad
**Evaluación IA:** CUMPLE
**Justificación IA:** Desde el historial se puede:

crear consulta;
prescribir;
editar una entrada propia;
volver mediante breadcrumbs.

**Decisión del Grupo:** DE ACUERDO


## H4 — Consistencia
**Evaluación IA:** CUMPLE
**Justificación IA:** Utiliza el mismo:

navbar;
paciente;
breadcrumb;
sistema de botones;
tarjetas;
tipografía;
colores.

**Decisión del Grupo:** DE ACUERDO


## H5 — Prevención de errores
**Evaluación IA:** CUMPLE
**Justificación IA:** La propia interfaz evita ofrecer "Editar" para una entrada que pertenece a otro profesional. No solamente se informa el problema: se evita presentar una acción que el usuario no puede ejecutar.
**Decisión del Grupo:** DE ACUERDO


## H6 — Reconocimiento antes que recuerdo
**Evaluación IA:** CUMPLE
**Justificación IA:** Toda la información relevante está visible en la propia pantalla.

El veterinario no tiene que recordar:

qué paciente está viendo;
quién creó la entrada;
qué peso tenía;
qué diagnóstico se registró;
si la entrada fue modificada.

**Decisión del Grupo:** DE ACUERDO


## H7 — Flexibilidad y eficiencia
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:**  La pantalla permite acceder rápidamente a:

Nueva Consulta
Prescribir Medicación
Editar esta Entrada

Sin embargo, cuando el historial crezca considerablemente, esta vista puede volverse larga y poco eficiente.

Pero esto no está demostrado como problema en el mockup actual, porque el escenario trabajado no especifica historiales masivos.
**Decisión del Grupo:** Si bien como grupo se comprende el problema, solucionarlo implicaria inclumpir con las consignas del TP2: "no deben agregar historias nuevas ni pantallas no respaldadas por TP1".


## H8 — Diseño estético/minimalista
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** La información es necesaria, pero cada entrada muestra bastantes datos simultáneamente.

Sin embargo, el uso de:

<details>

para la explicación de RF-08 es una buena decisión porque permite ocultar información secundaria.

Por eso no lo considero incumplimiento.
**Decisión del Grupo:** Elegimos como grupo no ahcer este tipo de modificaciones para basarnos más en la funcionalidad que en la estética.


## H9 — Recuperación ante errores
**Evaluación IA:** CUMPLE
**Justificación IA:** Si el usuario intenta editar una entrada que no corresponde:

flash("Solo el profesional autor de la entrada puede editarla...")

y vuelve al historial.

Además, el historial muestra quién puede editar.
**Decisión del Grupo:** DE ACUERDO


## H10 — Ayuda/documentación
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** o existe ayuda para conceptos como:

qué significa "Modificada";
qué representa cada dato;
qué hacer si existe una inconsistencia.
**Decisión del Grupo:** Consdieramos que explicitar cada dato es demasiado extenso y repercutiría en la heurística 8, minimalismo.
