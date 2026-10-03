## H1 — Visibilidad del estado
**Evaluación IA:** INCUMPLE
**Justificación IA:** Cuando se detecta la interacción se muestra:

ALERTA CRÍTICA: Incompatibilidad Medicamentosa Detectada

Eso está bien.

Pero la interfaz presenta una situación interactiva sin garantizar que las acciones asociadas funcionen.

Además, no queda visualmente suficientemente claro si:

la prescripción fue cancelada;
quedó pendiente;
se requiere justificación;
se puede continuar.

La intención está escrita, pero la interacción está mal conectada.
**Decisión del Grupo:** DE ACUERDO, SE DEBE CAMBIAR PARA CUMPLIR CON LA HEURÍSTICA


## H2 — Correspondencia con mundo real
**Evaluación IA:** CUMPLE
**Justificación IA:** Los términos son adecuados
**Decisión del Grupo:** DE ACUERDO


## H3 — Control y libertad del usuario
**Evaluación IA:** INCUMPLE
**Justificación IA:** Este es uno de los problemas principales.

La interfaz presenta:

<button ...>Continuar Bajo Mi Responsabilidad Profesional</button>
<button ...>Cancelar Prescripción</button>

pero están fuera del <form>.

Por lo tanto, el usuario percibe que puede decidir, pero la estructura HTML no garantiza que esas acciones ejecuten el flujo previsto.
**Decisión del Grupo:** Hallazgo aceptado, se debe solucionar


## H4 — Consistencia y estándares
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** Visualmente sigue el sistema.

Pero hay una inconsistencia importante:

En las otras pantallas, los controles de la operación están contenidos dentro del formulario correspondiente.

En esta pantalla, la alerta tiene controles de formulario separados del formulario.
**Decisión del Grupo:** Deriva del mismo problema que H3, se solucionará en conjunto.


## H5 — Prevención de errores
**Evaluación IA:** NCUMPLE
**Justificación IA:** Esta pantalla debería ser justamente la que más prevención proporcione.

El flujo correcto es:

Intentar prescribir
        ↓
Detectar interacción
        ↓
Advertir
        ↓
Solicitar justificación
        ↓
Cancelar o continuar

Actualmente la interfaz visualiza ese flujo, pero los controles de la alerta no están correctamente asociados al formulario.

Además, la justificación no tiene:

required

y la única validación efectiva es del servidor.
**Decisión del Grupo:** Hallazgo aceptado, se debe cambiar.


## H6 — Reconocimiento antes que recuerdo
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** La alerta informa explícitamente:

Conflicto detectado con el tratamiento activo

y muestra el medicamento conflictivo y el efecto adverso.

Eso está muy bien.

Pero el usuario debe interpretar por sí mismo qué hacer con la alerta.

Podemos mejorar esto haciendo explícita la secuencia:

Para continuar, escribí una justificación clínica y seleccioná "Continuar".
**Decisión del Grupo:** Un hallazgo interesante, se acepta, se puede cambiar.


## H7 — Flexibilidad y eficiencia
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** Hay un buen diseño porque no obliga al veterinario a abandonar el flujo.

Puede:

cancelar;
justificar y continuar.

Pero el flujo actual tiene el problema estructural de los botones.
**Decisión del Grupo:** Se mejorará el flujo.


## H8 — Diseño estético y minimalista
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** La alerta es deliberadamente prominente y eso está justificado porque se trata de un riesgo clínico.

Pero hay bastante información:

tratamiento activo;
tipo;
fármaco;
dosis;
indicaciones;
vigencia;
alerta;
justificación;
acciones.

No es necesariamente incorrecto, pero la alerta podría jerarquizar mejor qué debe leer primero.
**Decisión del Grupo:** Se considera que toda la información presentada es altamente relevante para el sistema. Se rechaza el hallazgo, no hay cambios


## H9 — Recuperación ante errores 
**Evaluación IA:** INCUMPLE
**Justificación IA:** La interacción medicamentosa constituye precisamente una condición en la que el sistema debe ayudar al usuario a recuperarse de una acción potencialmente peligrosa.

La interfaz tiene la información necesaria, pero la interacción de los botones está mal implementada.

Además, cuando la justificación es inválida:

{% if errores.get('justificacion') %}

el mensaje no tiene id ni relación explícita con el textarea.
**Decisión del Grupo:** Se acepta el hallazgo, debe haber cambios


## H10 — Ayuda y documentación
**Evaluación IA:** CUMPLE PARCIALMENTE
**Justificación IA:** Hay bastante ayuda contextual mediante:

placeholder="Ejemplo: ..."

y la explicación del conflicto.

Pero sería conveniente que la propia alerta explicara brevemente:

Para continuar bajo responsabilidad profesional se requiere una justificación clínica.
**Decisión del Grupo:** No se acepta, se considera que la información es necesaria.
