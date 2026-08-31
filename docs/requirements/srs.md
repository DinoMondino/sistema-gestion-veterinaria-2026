# Software Requirements Specification - **Proyecto sistema de gestión veterinaria**

## Visión general del proyecto y alcance
### Dominio y Problema
La fragmentación y falta de trazabilidad en los historiales clínicos veterinarios, lo que dificulta el manejo de la heterogeneidad de especies, razas y patologías.
Afecta a médicos veterinarios, asistentes, animales y propietarios o productores agropecuarios.
La resolución actual es mediante historias clínicas en papel, planillas de cálculo dispersas o software rígido que no se adapta con flexibilidad a las distintas especies (mascotas pequeñas y animales de campo).

### Tipos de datos
* Datos de identificación de personas: dueños de mascotas (nombre, contacto, dirección), personal de la clínica.
* Datos de las mascotas: especie, raza, fecha de nacimiento, sexo.
* Clínicos, biológicos y transaccionales (historiales de peso, vacunas, patologías, planes sanitarios, interacciones medicamentosas y datos de identificación de tutores/productores).
Tienen origen en: Ingreso manual en consulta por parte del profesional y referencias estructuradas externas.
Formato: Datos estructurados relacionales (tablas en base de datos SQL, JSON/CSV) y texto libre para observaciones clínicas específicas.

### Valor del Sistema
Centraliza en un entorno seguro la información clínica heterogénea tanto para pacientes individuales (mascotas) como para rodeos, majadas o lotes completos de animales de producción. También facilita el control estricto de los tiempos de carencia de los medicamentos (período obligatorio antes de la faena o el ordeñe), asegurando normativas sanitarias y protegiendo la salud pública.
Permite planificar, ejecutar y evaluar vacunaciones y tratamientos a gran escala de forma rápida, reemplazando planillas dispersas del ámbito rural y reduce el riesgo de errores en prescripciones y dosis masivas, proporcionando una herramienta ágil y confiable.
Si el sistema funciona la secretaria arma la agenda del día sin llamar por teléfono para confirmar historiales; el veterinario accede a la historia clínica completa de la mascota en el momento de la consulta y puede indagar patologías hereditarias/genéticas en OMIA sin salir del flujo de trabajo; el dueño deja de depender de su propia memoria para saber historial, necesidades o plazos y puede consultar pagos e historial sin llamar a la veterinaria.

### Alcance Realista
Dentro del alcance en el cuatrimestre:
  * Registro de pacientes tanto individuales (mascotas) como por lotes/rodeos (animales de campo).
  * Agenda de turnos (crear, ver, cancelar).
  * Historial básico de vacunas, peso y consultas clínicas.
  * Registro de pagos asociados a consultas (sin facturación fiscal).
  * Módulo funcional de alertas para interacciones medicamentosas elementales y control básico de fechas sanitarias.
  * Consulta de referencia a OMIA sobre patologías (solo lectura/enlace, sin sincronización completa de la base).
  * Roles y permisos diferenciados por perfil de usuario.

Fuera del alcance inicial:
  * Atención de animales grandes (equinos, bovinos, etc.) — se decidió limitar el sistema a mascotas/animales pequeños porque atender animales grandes implica un servicio veterinario completamente distinto (visitas a campo, manejo, infraestructura), no una simple extensión de datos.
  * Facturación electrónica / integración con AFIP.
  * Gestión de inventario de medicamentos/insumos.
  * Soporte multi-clínica o múltiples sucursales.
  * Adjuntar estudios/imágenes a la historia clínica.
  * Sincronización completa/local de la base OMIA (se consulta como referencia externa).
  * Planes sanitarios masivos o campañas de vacunación poblacional (el sistema hace seguimiento individual por mascota, no gestión epidemiológica agregada).
  * Integración con equipos de diagnóstico de laboratorio.
  * Modelos predictivos de diagnóstico por IA.
  
### Riesgos de Fracaso y Mitigación
El riesgo más probable en este proyecto puntual es la negociación de requerimientos entre stakeholders con intereses distintos: secretaría, veterinario y dueño van a pedir cosas distintas del mismo sistema (por ejemplo, cuánta información clínica debería poder ver un dueño, o si la secretaria puede registrar una vacuna sin supervisión del veterinario). Para mitigarlo, se definieron roles y permisos desde el modelo de dominio, y cada historia de usuario está atada a un único rol responsable de la acción, dejando explícito qué puede y qué no puede hacer cada perfil.

Un riesgo secundario es la incertidumbre técnica de la integración con OMIA, al no tratarse de una API pensada para integración directa. Se mitiga tratándola como un incremento aislado y de alcance reducido (consulta/enlace), postergable sin afectar el resto del sistema.

### Datos Sensibles
El sistema maneja datos personales identificables tanto de tutores de mascotas como de productores agropecuarios o arrendatarios (nombre, DNI, CUIT/CUIL, teléfono, ubicación geoespacial del campo, datos de contacto y comerciales). Conforme al Código de Ética IEEE/ACM y la legislación vigente de protección de datos personales, esto implica la obligación absoluta de garantizar medidas rigurosas de confidencialidad, controles de acceso estrictos basados en roles y el uso exclusivo de la información para fines clínicos y sanitarios autorizados.

## Módulo stakeholders y roles identificados
### Perfiles de Usuarios Directos
* Médico veterinario: Crea y edita historias clínicas, receta tratamientos, registra procedimientos, evalúa interacciones y planifica intervenciones individuales o masivas.
* Asistente / Recepcionista: Registra altas de nuevos pacientes, gestiona turnos básicos y administra el ingreso administrativo inicial.
* Dueño de Mascota/Animal de Campo: Clientes habituales. Solicitud de turnos, consulta de historia clínica y pagos de su mascota

### Stakeholders Indirectos
* Asesores técnicos / Ingenieros agrónomos: Analizan el rendimiento productivo global del establecimiento cruzando los datos sanitarios provistos por el sistema.
* Autoridades sanitarias y organismos de control: Interesados en la trazabilidad estricta, cumplimiento de vacunaciones obligatorias y control de tiempos de carencia en animales de consumo.
* Frigoríficos y Plantas de Faena: Requieren garantías sobre la trazabilidad de tratamientos e historial sanitario para asegurar la inocuidad alimentaria.
* SENASA / normativa sanitaria animal: Define esquemas de vacunación obligatoria (ej. rabia) que el calendario de vacunación debe poder reflejar; interesada en la trazabilidad epidemiológica ante campañas de vacunación masiva o control de brotes.


> Quedó deliberadamente fuera de esta primera versión un cuarto perfil de "administrador de la clínica" independiente del veterinario — se decidió fusionar ese rol con el de veterinario/a para no multiplicar roles antes de validar los tres principales.

---
## Lista de requerimientos funcionales
* [Requerimientos funcionales](RF.md): Proceso Seleccionado: Gestión Clínica e Historial
---
## Casos de uso
* [Casos de Uso](use-cases.md): Descripción detallada de los flujos de interacción con el sistema
---
## Historias de usuario
* [Historias de Usuario (HUs)](user-stories.md): Requerimientos funcionales centrados en el valor de los usuarios del proceso elegido.
---
## Slices
* 
## Atributos de calidad
* [Atributos de Calidad](quality-attributes.md): Requerimientos no funcionales (rendimiento, seguridad, usabilidad).
