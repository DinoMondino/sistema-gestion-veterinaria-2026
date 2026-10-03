## H1 — Visibilidad del estado del sistema
**Evaluación de la IA:** CUMPLE PARCIALMENTE

**Justificación IA:** La pantalla muestra correctamente el estado después de una operación para errores y mediante flash() después de guardar correctamente.

Además, cuando hay errores se informa:

"No se pudo guardar la consulta"

y se conserva la información introducida. El problema es que la interfaz no tiene un estado explícito mientras se procesa el guardado.

**Consideración del grupo:** No se cree necesario que haya un mensaje de "Guardando..." mientras se da el proceso

## H2 — Correspondencia entre sistema y mundo real
**Evaluación IA:** CUMPLE

**Justifiación IA:** La pantalla utiliza términos que corresponden directamente al trabajo veterinario. No aparecen términos técnicos de programación ni nombres internos del sistema.
Además, el perfil establece explícitamente que se debe utilizar terminología relacionada con la gestión clínica veterinaria.

**Consideración del Grupo:** DE ACUERDO



## H3 - Control y libertad del usuario
**Evaluación de la IA:** CUMPLE

**Justificación IA:** El veterinario puede:

cargar información;
guardar;
cancelar y volver al historial.

Además, el script global detecta modificaciones no guardadas

**Consideración del grupo:** DE ACUERDO.


## H4 — Consistencia y estándares
**Evaluación de la IA:** CUMPLE 

**Justificación IA:** Los elementos siguen los patrones visuales del resto:

mismos botones;
mismos campos;
mismas tarjetas;
mismo breadcrumb;
mismo encabezado;
misma información del paciente.

La pantalla utiliza además label asociados correctamente mediante for/id.

**Consideración del grupo:** DE ACUERDO


## H5 — Prevención de errores
**Evaluación de la IA:** CUMPLE PARCIALMENTE

**Justificación IA:** La prevención ocurre principalmente después de enviar el formulario.

Además, _campos.html no marca como required los campos obligatorios.
La aplicación puede detectar el error, pero el navegador no ayuda a prevenirlo antes del envío.

**Consideración del grupo:** Consideramos que es correcto lo planteado, por lo que debe hacerse un cambio. El hallazgo de la IA acepta.


## H6 — Reconocimiento antes que recuerdo
**Evaluación de la IA:** CUMPLE

**Justificación IA:** Los campos están explícitamente etiquetados. y además hay ayudas:

Ejemplo: 6.8

Describí detalladamente los signos clínicos

Diagnóstico de trabajo o hipótesis principal

El usuario no tiene que recordar qué debe introducir.

**Consideración del grupo:** DE ACUERDO


## H7 — Flexibilidad y eficiencia de uso
**Evaluación de la IA:** CUMPLE

**Justificación IA:** La pantalla tiene:

estructura en dos/tres columnas;
atajo Ctrl + Enter;
datos del paciente visibles;
navegación por breadcrumb;
campos agrupados.

Para un veterinario que realiza repetidamente consultas, esto reduce pasos.

**Consideración del grupo:** DE ACUERDO



## H8 — Diseño estético y minimalista
**Evaluación de la IA:** CUMPLE

**Justificación IA:** La información está agrupada. Esto es especialmente apropiado porque el formulario tiene varios campos.

No se agregan elementos decorativos irrelevantes.

**Consideración del grupo:** DE ACUERDO


## H9 — Ayudar a reconocer, diagnosticar y recuperarse de errores
**Evaluación de la IA:** CUMPLE

**Justificación IA:** El sistema indica:

No se pudo guardar la consulta

muestra cantidad de errores y además genera enlaces que llevan al campo correspondiente.

También conserva lo que el usuario había escrito.

**Consideración del grupo:** DE ACUERDO


## H10 — Ayuda y documentación
**Evaluación de la IA:** CUMPLE

**Justificación IA:** No existe un manual enorme, pero la pantalla proporciona ayuda contextual suficiente mediante

**Consideración del grupo:** DE ACUERDO.
