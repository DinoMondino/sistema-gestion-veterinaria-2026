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