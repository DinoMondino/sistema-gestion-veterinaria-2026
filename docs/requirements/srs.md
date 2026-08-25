# Software Requirements Specification

## Módulo stakeholders y roles identificados
### Perfiles de Usuarios Directos
* Médico veterinario: Crea y edita historias clínicas, receta tratamientos, registra procedimientos, evalúa interacciones y planifica intervenciones individuales o masivas.
* Asistente / Recepcionista: Registra altas de nuevos pacientes, gestiona turnos básicos y administra el ingreso administrativo inicial.
* Productor agropecuario o encargado de campo: Registra eventos rápidos (nacimientos, aplicación de planes sanitarios masivos, movimientos de hacienda entre potreros o control de peso), utilizando interfaces simplificadas o dispositivos móviles.

### Stakeholders Indirectos
* Propietarios de Mascotas y Productores: Interesados directos en la trazabilidad, salud y rendimiento de sus animales.
* Asesores técnicos / Ingenieros agrónomos: Analizan el rendimiento productivo global del establecimiento cruzando los datos sanitarios provistos por el sistema.
* Autoridades sanitarias y organismos de control: Interesados en la trazabilidad estricta, cumplimiento de vacunaciones obligatorias y control de tiempos de carencia en animales de consumo.
* Frigoríficos y Plantas de Faena: Requieren garantías sobre la trazabilidad de tratamientos e historial sanitario para asegurar la inocuidad alimentaria.

---
## Módulo canvas de descubrimiento y alcance
### Dominio y Problema
* Problema: La fragmentación y falta de trazabilidad en los historiales clínicos veterinarios, lo que dificulta el manejo de la heterogeneidad de especies, razas y patologías.
* Afectados: Médicos veterinarios, asistentes, animales y productores agropecuarios.
* Situación actual: Se resuelve mediante historias clínicas en papel, planillas de cálculo dispersas o software rígido que no se adapta con flexibilidad a las distintas especies (mascotas pequeñas y animales de campo).

### Tipos de datos
Clínicos, biológicos y transaccionales (historiales de peso, vacunas, patologías, planes sanitarios, interacciones medicamentosas y datos de identificación de tutores/productores).
* Origen: Ingreso manual en consulta por parte del profesional y referencias estructuradas externas.
* Formato: Datos estructurados relacionales (tablas en base de datos SQL, JSON/CSV) y texto libre para observaciones clínicas específicas.

### Valor del Sistema
* Centraliza en un entorno seguro la información clínica heterogénea tanto para pacientes individuales (mascotas) como para rodeos, majadas o lotes completos de animales de producción. También facilita el control estricto de los tiempos de carencia de los medicamentos (período obligatorio antes de la faena o el ordeñe), asegurando normativas sanitarias y protegiendo la salud pública.
* Permite planificar, ejecutar y evaluar vacunaciones y tratamientos a gran escala de forma rápida, reemplazando planillas dispersas del ámbito rural y reduce el riesgo de errores en prescripciones y dosis masivas, proporcionando una herramienta ágil y confiable.

### Alcance Realista
Dentro del alcance en el cuatrimestre:
  * Registro de pacientes tanto individuales (mascotas) como por lotes/rodeos (animales de campo).
  * Historial básico de vacunas, peso y consultas clínicas.
  * Módulo funcional de alertas para interacciones medicamentosas elementales y control básico de fechas sanitarias.
Fuera del alcance inicial:
  * Gestión avanzada de trazabilidad oficial integrada con APIs de organismos de control.
  * Aplicaciones móviles nativas con sincronización offline.
  * Integración con equipos de laboratorio complejos, IA predictiva y facturación comercial completa.

### Riesgos de Fracaso y Mitigación
Lo mas riesgoso del proyecto es la incertidumbre inicial y dificultad de modelar una arquitectura de datos que soporte simultáneamente el seguimiento individual (mascotas) y masivo (campo) considerando la diversidad de especies sin caer en el sobrediseño.
Se busca mitigar r ealizando validaciones tempranas con profesionales veterinarios para acotar el modelo a lo esencial y utilizando un enfoque incremental para construir primero las funciones base.

### Datos Sensibles
El sistema maneja datos personales identificables tanto de tutores de mascotas como de productores agropecuarios o arrendatarios (nombre, DNI, CUIT/CUIL, teléfono, ubicación geoespacial del campo, datos de contacto y comerciales). Conforme al Código de Ética IEEE/ACM y la legislación vigente de protección de datos personales, esto implica la obligación absoluta de garantizar medidas rigurosas de confidencialidad, controles de acceso estrictos basados en roles y el uso exclusivo de la información para fines clínicos y sanitarios autorizados.

---

## Índice
* [Historias de Usuario (HUs)](user-stories.md): Requerimientos funcionales centrados en el valor de los usuarios.
* [Casos de Uso](use-cases.md): Descripción detallada de los flujos de interacción con el sistema.
* [Atributos de Calidad](quality-attributes.md): Requerimientos no funcionales (rendimiento, seguridad, usabilidad).
