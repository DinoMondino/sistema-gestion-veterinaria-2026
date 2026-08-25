# Atributos de Calidad (ISO 25010)

Los requerimientos no funcionales del sistema se especifican mediante **Atributos de Calidad** basados en el modelo **ISO/IEC 25010**. Cada atributo se evalúa a través de escenarios de calidad estructurados que consideran múltiples condiciones de entorno (operación normal, alta concurrencia por campañas sanitarias masivas, y trabajo a campo bajo luz solar o conectividad limitada).

---
## 1. Eficiencia de Desempeño (Performance Efficiency)

Evalúa el comportamiento del sistema frente al procesamiento masivo de datos (como el registro de lotes de animales en establecimientos de campo) y la consulta rápida de historiales clínicos.
### Escenario 1.1: Consulta individual en entorno clínico estándar
* Fuente: Médico Veterinario.
* Estímulo: Solicita la visualización del historial clínico completo de un paciente individual (mascota).
* Artefacto: Módulo de base de datos y interfaz de consulta clínica.
* Entorno: Operación diaria normal, con conectividad estable de banda ancha en consultorio y baja concurrencia simultánea en el servidor.
* Respuesta: El sistema recupera y muestra el historial completo (pesos, vacunas, consultas previas).
* Medida: El tiempo de respuesta de la interfaz es menor a 1.5 segundos.

### Escenario 1.2: Carga masiva de datos sanitarios en entorno rural de alta concurrencia
* Fuente: Productor Agropecuario / Asistente de campo.
* Estímulo: Sube o registra simultáneamente datos de un plan sanitario masivo (vacunación de un rodeo de más de 500 animales) desde un dispositivo móvil.
* Artefacto: Módulo de transacciones masivas y API backend.
* Entorno: Período crítico de campaña sanitaria a campo, con alta concurrencia de múltiples productores registrando eventos en paralelo y conectividad móvil fluctuante (4G/3G).
* Respuesta: El sistema procesa los registros por lotes, valida las reglas de negocio y almacena la información sin bloquear las conexiones concurrentes.
* Medida: El procesamiento completo del lote de 500 registros se efectúa en menos de 5 segundos, con una tasa de éxito de transacciones del 100% y sin pérdida de datos ante intermitencias de red.

---
## 2. Seguridad (Security / Confidentiality & Integrity)

Este atributo garantiza la protección de los datos sensibles (información personal de tutores y productores, datos fiscales y trazabilidad sanitaria) frente a accesos no autorizados.
### Escenario 2.1: Control de acceso basado en roles en entorno de oficina
* Fuente: Usuario con rol de Asistente / Recepcionista.
* Estímulo: Intenta acceder a módulos restringidos de modificación de diagnósticos médicos o datos financieros/fiscales sensibles de los productores.
* Artefacto: Subsistema de autenticación, control de accesos (RBAC) y encriptación de base de datos.
* Entorno: Operación normal en red interna de la veterinaria con credenciales válidas pero de privilegios limitados.
* Respuesta: El sistema deniega el acceso a las funciones avanzadas y muestra una advertencia de permisos insuficientes, registrando el intento en el log de auditoría.
* Medida: Bloqueo inmediato del acceso no autorizado en el 100% de los intentos y registro auditable en menos de 0.2 segundos.

### Escenario 2.2: Intento de filtración o acceso externo no autorizado a datos sensibles
* Fuente: Actor externo / Usuario no autenticado.
* Estímulo: Intenta extraer datos identificables de tutores o ubicaciones geoespaciales de campos mediante peticiones maliciosas directas a los endpoints de la API.
* Artefacto: Capa de seguridad de la API, políticas de CORS y validación de tokens JWT.
* Entorno: Conexión pública externa con intentos de ataques de enumeración o inyección.
* Respuesta: El sistema rechaza las peticiones no autenticadas, encripta los datos sensibles en tránsito (HTTPS/TLS 1.3) y en reposo (AES-256).
* Medida: Cero exposición de datos sensibles y rechazo del 100% de las solicitudes que carezcan de un token válido o que presenten anomalías de formato.

---
## 3. Usabilidad (Usability / Operability)

Este atributo asegura que el software sea intuitivo y eficiente tanto para profesionales en entornos clínicos bajo presión como para operadores en el ámbito rural.
### Escenario 3.1: Alta carga de trabajo en urgencia clínica
* Fuente: Médico Veterinario.
* Estímulo: Requiere registrar de urgencia el peso actual y una medicación crítica durante una consulta de emergencia.
* Artefacto: Interfaz de usuario de carga rápida de consultas.
* Entorno: Alta presión temporal y estrés operativo en la clínica veterinaria, requiriendo minima fricción visual.
* Respuesta: El formulario presenta campos dinámicos simplificados que permiten completar el registro en pocos clics sin navegar por menús complejos.
* Medida: El veterinario completa el registro crítico en menos de 30 segundos sin requerir asistencia o manual de usuario.
