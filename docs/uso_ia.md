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
