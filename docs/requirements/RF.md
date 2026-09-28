# Requerimientos funcionales
## Proceso Seleccionado: Gestión Clínica e Historial
*RF-01:* El sistema debe permitir registrar una nueva consulta clínica asociada a un paciente individual, indicando fecha, síntomas detectados, diagnóstico preliminar y observaciones en texto libre.

*RF-02:* El sistema debe permitir registrar y almacenar el peso actual de un paciente durante la consulta clínica para su seguimiento temporal.

*RF-03:* El sistema debe permitir registrar la aplicación de vacunas especificando el nombre de la medicación, el por qué de su aplicación, número de lote, fecha de aplicación y fecha de próximo vencimiento.

*RF-04:* El sistema debe permitir asociar y registrar patologías existentes o potenciales al historial clínico del paciente.

*RF-05:* El sistema debe permitir registrar los procedimientos clínicos realizados por el profesional durante la atención del paciente.

*RF-06:* El sistema debe permitir registrar, actualizar y dar de baja las medicaciones activas y suplementaciones prescriptas en el plan de tratamiento del paciente.

*RF-07:* El sistema debe permitir consultar el historial clínico cronológico completo de un paciente, integrando en una vista unificada consultas, pesos, vacunas, patologías y procedimientos.

*RF-08:* El sistema debe permitir al médico veterinario editar o corregir entradas previas dentro del historial clínico bajo su validación exclusiva de rol.

*RF-09:* El sistema debe permitir realizar búsquedas y enlaces de referencia de lectura directa hacia la base de datos externa OMIA utilizando términos de patologías animales.

*RF-10:* El sistema debe validar que los datos obligatorios del registro clínico cumplan con los formatos y rangos esperados (como fechas válidas y valores numéricos positivos para el peso) antes de confirmar su almacenamiento.

*RF-11:* El sistema debe informar al usuario los errores de validación encontrados al intentar guardar un registro clínico incompleto o con datos inválidos, indicando con precisión el campo y el motivo del fallo.

*RF-12:* El sistema debe permitir generar gráficos o reportes tabulares de la evolución cronológica del peso del paciente a partir de los datos históricos almacenados.

# Atributos de calidad

## Atributos Elegidos y justificación:

Operabilidad, (Capacidad de interacción):"El sistema es fácil de operar y controlar"
hay tres perfiles con contextos muy distintos. El más exigente es el veterinario, que registra datos en plena atención, muchas veces con las manos ocupadas y sin tiempo para navegar menús. Si registrar es lento, el dato se carga tarde o de memoria, y la historia clínica pierde calidad.

Integridad,(Seguridad de la Información): "Se impide la modificación no autorizada de datos y del sistema"
la historia clínica es el activo central del sistema. Un dato clínico alterado por alguien sin el rol adecuado puede llevar a una decisión médica errónea. Además, RF-08 limita la edición de entradas previas al veterinario, y esa restricción tiene que valer en el servidor y no solo en la interfaz.

Capacidad de Recuperación, (Fiabilidad) "El sistema se recupera de una falla, restablece el servicio y restaura los datos afectados"
una consulta no se puede volver a hacer, y la clínica no tiene un sistema alternativo. Perder o dejar corrupta la base de datos es la falla más costosa, y con infraestructura modesta es una falla esperable, no una rareza.

Responsabilidad, (Seguridad de la información): "Las acciones de cada entidad pueden rastrearse hasta ella"
las entradas clínicas tienen valor profesional y pueden corregirse (RF-08). En una clínica pequeña es habitual compartir equipos y sesiones, así que sin atribución individual no se puede saber quién registró o cambió qué.

Modificabilidad, (Mantenibilidad): "Se puede modificar el sistema sin introducir defectos ni degradar la calidad"
el proyecto es incremental y el SRS declara que los requerimientos evolucionan; además depende de OMIA, un servicio externo que el equipo no controla. Que cada cambio quede acotado es lo que hace viable el ciclo de vida elegido

---
## Slices: Historias de usuario + Casos de uso
* [Historias de Usuario + Casos de uso](slices.md): Requerimientos funcionales centrados en el valor de los usuarios del proceso elegido.

---
## Escenarios de los atributos de calidad
* [Escenarios](quality-scenarios.md)