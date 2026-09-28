---
## 2. Escenarios

### Atributo 1 — Operabilidad

#### Escenario 1.1 — Registro de una consulta en una urgencia clínica

| Componente | Descripción |
|---|---|
| **Fuente** | Médico/a veterinario/a |
| **Estímulo** | Necesita registrar el peso del paciente y una medicación mientras sostiene al animal |
| **Artefacto** | Formulario de registro de consulta |
| **Entorno** | **Degradado:** urgencia clínica, presión de tiempo, una sola mano libre, tablet del consultorio y sin posibilidad de consultar un manual |
| **Respuesta** | El formulario muestra primero los campos críticos (peso, fármaco, dosis) con teclado numérico y el último peso registrado como referencia; permite guardar con solo los campos obligatorios y completar el resto después; ante un error de validación, marca el campo y conserva todo lo ingresado |
| **Medida** | Registro crítico completado en ≤ 45 s y ≤ 8 interacciones, sin cambiar de pantalla, con veterinarios sin capacitación previa (≥ 90% de las pruebas); 0 pérdidas de datos ante un error de validación |

- **¿Por qué es crítico?:** es el momento de mayor presión del flujo clínico y donde una interfaz torpe empuja a cargar los datos, después, de memoria.
- **Impacto en la arquitectura:** hay que definir qué campos son obligatorios en el guardado inicial y cuáles se completan luego, lo que se relaciona con la edición posterior (RF-08); el estado del formulario debe conservarse ante errores.


### Atributo 2 — Integridad

#### Escenario 2.1 — Petición de modificación clínica que saltea la interfaz

| Componente | Descripción |
|---|---|
| **Fuente** | Usuario autenticado con rol de Secretario/a o de Tutor/a |
| **Estímulo** | Envía directamente al servidor una petición para modificar el diagnóstico de una consulta, salteando la interfaz que oculta esa opción a su rol |
| **Artefacto** | Capa de autorización del servidor sobre el historial clínico |
| **Entorno** | **Degradado:** uso indebido con credenciales válidas de rol limitado y una petición manipulada que no proviene de la interfaz |
| **Respuesta** | El servidor valida rol y recurso, rechaza la petición, no modifica ningún dato y registra el intento |
| **Medida** | 100% de las peticiones no autorizadas rechazadas; 0 registros modificados; evento registrado en ≤ 1 s con usuario, acción y recurso |

- **¿Por qué es crítico?:** las restricciones aplicadas solo en la interfaz son triviales de eludir; un diagnóstico alterado por alguien sin rol clínico compromete decisiones médicas.
- **Impacto en la arquitectura:** la autorización se decide en el servidor, por rol y por recurso, en cada operación de escritura, y no puede delegarse a la interfaz.


### Atributo 3 — Capacidad de recuperación

#### Escenario 3.1 — Caída de la base de datos en plena jornada

| Componente | Descripción |
|---|---|
| **Fuente** | Falla de hardware o error operativo en el servidor de base de datos |
| **Estímulo** | La base de datos queda inaccesible o corrupta a media mañana |
| **Artefacto** | Base de datos y mecanismo de respaldo |
| **Entorno** | **Degradado:** falla total de la persistencia durante el horario de atención, con turnos en curso |
| **Respuesta** | Se restaura el servicio desde el último respaldo más el registro de transacciones; mientras tanto se muestra un aviso de mantenimiento; al restablecerse se verifica la consistencia de los datos y se informa qué se recuperó |
| **Medida** | RTO ≤ 4 h; RPO ≤ 15 min (pérdida máxima de datos ya confirmados); 0 registros huérfanos tras la verificación; restauración de prueba ejecutada al menos una vez por etapa del proyecto |

- **¿Por qué es crítico?:** perder un día de historias clínicas no es recuperable por otra vía, y la clínica no tiene sistema alternativo.
- **Impacto en la arquitectura:** base de datos con recuperación a un punto en el tiempo, respaldos fuera del servidor principal y un procedimiento de restauración probado y documentado.


### Atributo 4 — Responsabilidad (accountability)

#### Escenario 4.1 — Corrección de una entrada histórica del historial

| Componente | Descripción |
|---|---|
| **Fuente** | Médico/a veterinario/a |
| **Estímulo** | Corrige el diagnóstico de una consulta registrada semanas atrás, que el tutor ya recibió |
| **Artefacto** | Edición del historial clínico y registro de auditoría |
| **Entorno** | **Condición significativa:** la entrada ya fue vista por terceros y puede haber un reclamo o una auditoría posterior |
| **Respuesta** | El sistema conserva la versión original, guarda la nueva con autor, fecha y hora y un motivo obligatorio, y el historial indica que la entrada fue modificada; los registros de auditoría no pueden editarse ni borrarse desde la aplicación |
| **Medida** | 100% de las ediciones reconstruibles (quién, cuándo, valor previo, valor nuevo, motivo); 0 ediciones aceptadas sin motivo; todo intento de alterar la auditoría es rechazado |

- **¿Por qué es crítico?:** la historia clínica es un documento con valor profesional; poder editarla sin dejar rastro equivale a poder reescribirla.
- **Impacto en la arquitectura:** el historial se modela como versionado (solo se agregan versiones, no se sobrescribe) y la auditoría se guarda en un almacén con permisos separados.


### Atributo 5 — Modificabilidad

#### Escenario 5.1 — OMIA cambia su formato o debe reemplazarse

| Componente | Descripción |
|---|---|
| **Fuente** | Proveedor externo (OMIA) o decisión del equipo de reemplazar la fuente |
| **Estímulo** | OMIA modifica la estructura de sus respuestas sin aviso, o se decide reemplazarla por otra base de referencia |
| **Artefacto** | Integración con OMIA |
| **Entorno** | **Degradado:** cambio inesperado, con el sistema en producción y a mitad de un incremento |
| **Respuesta** | El cambio queda confinado al adaptador de la integración; el resto del sistema (historia clínica, registro de consultas) no se modifica y las pruebas del adaptador detectan la incompatibilidad |
| **Medida** | Cambio implementado y desplegado por una persona en ≤ 2 días; 0 módulos fuera del adaptador modificados; pruebas de regresión de CU-01 sin cambios |

- **¿Por qué es crítico?:** es el mayor riesgo técnico declarado en el SRS y no está bajo control del equipo; si el acoplamiento es fuerte, cada cambio externo se propaga a todo el sistema.
- **Impacto en la arquitectura:** la integración se aísla detrás de una interfaz propia (adaptador), con un modelo interno independiente del formato de OMIA. Esto habilita tratarla como un incremento separado, como plantea el ciclo de vida.
