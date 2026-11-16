# Documento de Diseño Detallado — TP4 (Parte A)
**Asignatura:** Ingeniería del Software 2026 — Trabajo Práctico 4  
**Proceso:** Gestión Clínica e Historial  
**Historia de Usuario:** HU-02 — Edición de Entradas Previas del Historial Clínico  

---

## Parte A — Diseño detallado de la HU 

### Paso 1 — Ficha de la HU:  

### 1.1 Propósito
El propósito de este documento es especificar el **Diseño Detallado** para la historia de usuario **HU-01 ("Manejo de datos obligatorios incompletos o con formato inválido")**, perteneciente al proceso central de **Gestión Clínica e Historial**.
**Relevancia de Dominio:** HU-01 exige validación de autoría, completitud de registros clínicos, versionado de entidades mediante enlaces jerárquicos y persistencia atómica transaccional con bitácora de auditoría.

---

### 1.2 Historia de Usuario Elegida: HU-01
- **Identificador:** HU-01 (Deriva de: CU-01, slice A1 (RF-10 y RF-11)).
- **Nombre:** Manejo de datos obligatorios incompletos o con formato inválido.
- **Enunciado:**
  Como Médico Veterinario, quiero recibir una notificación precisa cuando intento guardar una consulta con campos obligatorios vacíos o datos con formato inválido, para poder corregirlos y asegurar la integridad de la historia clínica sin perder la información cargada.

---

### 1.3 Criterios de Aceptación (Given-When-Then)

Given: El veterinario está completando el formulario de nueva consulta y escribe un valor negativo en el campo de peso o deja la fecha en blanco.
When: El veterinario presiona el botón "Guardar Consulta".
Then: El sistema rechaza el almacenamiento, resalta en rojo el campo con error y muestra un mensaje indicando con precisión el motivo del fallo.

---

### 1.4 Tabla de Coherencia con el TP3

| Dimensión         | Contenido                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Funcionalidad** | HU-01, derivada de CU-01, slice A1; vinculada con RF-10 y RF-11\. Validar los datos antes de guardar, rechazar los inválidos e informar los errores.                                                                                                                                                                                                                                                            |
| **Estructura**    | Estilo cliente-servidor. Patrón MVC en la interfaz web y capas en la API clínica. Intervienen Vistas, Controladores de pantalla, Modelo de formulario, Cliente de la API, Controladores REST, Autenticación y autorización, Servicio de registro clínico, Validación de registros clínicos y Gestión de excepciones. Componente principal: Validación de registros clínicos, en la capa de servicios de la API. |
| **Calidad**       | EC-01: Operabilidad. Tácticas: mantener modelos de tarea, de usuario y del sistema; reducir sobrecarga. DA-02: interfaz MVC con conservación del formulario y devolución conjunta de errores por campo.                                                                                                                                                                                                         |
| **Dominio**       | Se utilizan Veterinario, Mascota, HistoriaClinica y Consulta para representar el profesional, el paciente, su historial y los datos de la consulta que se intenta registrar.                                                                                                                                                                                                                                    |
| **Verificación**  | Para la HU: ingresar peso negativo o fecha vacía y comprobar rechazo, mensaje específico, campo resaltado, ausencia de almacenamiento y conservación de datos. Para EC-01: comprobar 0 pérdidas de datos ante errores y medir el registro crítico en ≤ 45 segundos y ≤ 8 interacciones, con al menos 90 % de pruebas exitosas en las condiciones definidas por el escenario.                                    |

---

### 1.5 Entidades del Modelo de Dominio Intervinientes

Entidades involucradas en HU-01:

Entidad del TP1¿Interviene?Qué utiliza la HU de ellaLa HU la...**Usuario**IndirectamenteIdentidad y rol del usuario autenticado, mediante VeterinarioConsulta**Secretaria**NoNo participa en el registro clínico de esta HU—**Veterinario**SíProfesional que intenta registrar la consultaConsulta**DuenioMascota**NoLos datos del tutor no intervienen en la validación—**Mascota**SíIdentificación del paciente al que corresponde la consultaConsulta**HistoriaClinica**SíHistorial al que se asociaría la consultaConsulta (no modifica)**Consulta**SíFecha y demás datos clínicos, incluido el peso que debe validarseSe intenta crear (el guardado se rechaza)**Vacuna**NoNo se validan vacunas en este escenario—**AplicacionVacuna**NoNo se registra una aplicación de vacuna—**Turno**NoNo se gestiona la agenda—**Prescripcion**NoNo se registra una prescripción—**ReaccionAdversaRegistrada**NoNo se registra una reacción adversa—**Pago**NoNo corresponde al proceso de validación clínica—**PatologiaReferencia**NoNo se realiza una consulta a OMIA

---

## Paso 2 — Análisis tridimensional 

| Dimensión         | Elemento                     | Detalle                                                                                                                                                   |
| ----------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Funcionalidad** | Criterio de aceptación HU-01 | Si se intenta guardar una consulta con peso negativo o fecha vacía, se rechaza el almacenamiento, se identifica el campo inválido y se muestra su motivo. |
| **Estructura**    | Frontera                     | Formulario de nueva consulta (Vistas de la interfaz web).                                                                                                 |
| **Estructura**    | Control                      | Controladores de pantalla, Controladores REST y Servicio de registro clínico coordinan el envío, la validación y la respuesta.                            |
| **Estructura**    | Dominio                      | Consulta contiene los datos a validar; Mascota, HistoriaClinica y Veterinario proporcionan el contexto del registro.                                      |
| **Estructura**    | Validación                   | Validación de registros clínicos, en la capa de servicios, evalúa los datos y produce errores específicos por campo.                                      |
| **Calidad**       | EC-01 — Operabilidad         | Conservar los datos ante el rechazo y devolver los errores juntos, evitando que el veterinario deba repetir la carga. Se aplica DA-02.                    |

---

### 3.3 Diagrama de Robustez




---

### 3.4 Ubicación de Reglas de Negocio

| Regla                                                                  | Responsable                                    | Justificación                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------ |
| **RN-01:** La fecha obligatoria no puede estar vacía y debe ser válida | `ValidacionRegistrosClinicos`                  | Centraliza las validaciones autoritativas definidas por RF-10.           |
| **RN-02:** El peso debe ser un número positivo                         | `ValidacionRegistrosClinicos`                  | Verifica el rango permitido para el dato clínico.                        |
| **RN-03:** No se registra una consulta con datos inválidos             | `ServicioRegistroClinico`                      | Coordina el registro y evita invocar la persistencia cuando hay errores. |
| **RN-04:** Cada error debe identificar el campo y su motivo            | `ValidacionRegistrosClinicos`                  | Genera los errores por campo, conforme a RF-11.                          |
| **RN-05:** Los datos cargados deben conservarse ante el rechazo        | `ControladorPantalla` y `Modelo de formulario` | Conservan el estado del formulario, conforme a EC-01 y DA-02.            |

---

| Elemento del diagrama           | Componente del TP3                                                                | Capa o rol                                |
| ------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------- |
| **FormularioNuevaConsulta**     | `Vistas`                                                                          | Vista — MVC (Interfaz Web)                |
| **ControladorPantalla**         | `Controladores de pantalla`; utiliza `Modelo de formulario` y `Cliente de la API` | Controlador y apoyo — MVC (Interfaz Web)  |
| **ControladorREST**             | `Controladores REST`                                                              | Presentación — API Clínica                |
| **AutenticacionAutorizacion**   | `Autenticación y autorización`                                                    | Transversal — API Clínica                 |
| **ServicioRegistroClinico**     | `Servicio de registro clínico`                                                    | Servicios — API Clínica                   |
| **ValidacionRegistrosClinicos** | `Validación de registros clínicos`                                                | Servicios — API Clínica                   |
| **GestionExcepciones**          | `Gestión de excepciones`                                                          | Transversal — API Clínica                 |
| **Consulta**                    | `Validación de registros clínicos` / `Servicio de registro clínico`               | Entidad de dominio utilizada en servicios |
| **Mascota**                     | `Servicio de registro clínico`                                                    | Entidad de dominio                        |
| **HistoriaClinica**             | `Servicio de registro clínico`                                                    | Entidad de dominio                        |
| **Veterinario**                 | `Autenticación y autorización`                                                    | Entidad de dominio del profesional        |

---

### 3.5 Diagramas de Secuencia



---

#### Secuencia A: Camino de Éxito (Edición Versionada Atómica con Auditoría)


---

#### Secuencia B: Caminos de Rechazo (Autoría Inválida / Motivo Vacío / Rollback)



---

### 3.6 Asignación de Responsabilidades (Criterios GRASP)

| Responsabilidad | Clase Asignada | Criterio GRASP Aplicado | Justificación de Diseño |
| :--- | :--- | :--- | :--- |
| **Verificar token y rol de usuario** | `AuthMiddleware` | **Protector de Variaciones / Low Coupling** | Aísla la verificación HTTP/JWT de la lógica clínica. |
| **Coordinar el flujo de edición** | `ControladorConsulta` | **Controller (Controlador)** | Recibe DTOs HTTP, delega al servicio y retorna respuestas JSON. |
| **Orquestar el versionado y auditoría** | `ServicioRegistroClinico` | **High Cohesion (Alta Cohesión)** | Concentra la lógica de aplicación sin acoplarse a frameworks de persistencia. |
| **Validar que el motivo no esté vacío** | `VersionConsulta` | **Information Expert (Experto)** | La propia clase conoce el estado de sus atributos y valida su consistencia. |
| **Crear la versión N+1 enlazada** | `VersionConsulta` | **Creator (Creador)** | Conoce los atributos de la versión previa (`parent_version_id`) y genera el nuevo número de versión. |
| **Garantizar la atomicidad SQL** | `RepositorioConsultaORM` | **Pure Fabrication (Fabricación Pura)** | Abstrae el manejo de `session.commit()` y `session.rollback()` de SQLAlchemy. |

---

## 4. Modelo de Clases

### 4.1 Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class PantallaEdicionConsulta {
        -formulario: ModeloFormularioEdicion
        +capturar_datos()
        +mostrar_exito(version: int)
        +mostrar_error(mensaje: String)
    }

    class ControladorConsulta {
        -servicio: ServicioRegistroClinico
        +editar_consulta(id: String, dto: DTOEdicionConsulta) RespuestaHTTP
    }

    class DTOEdicionConsulta {
        +consulta_id: String
        +sintomas: String
        +diagnostico: String
        +prescripcion: String
        +motivo_edicion: String
    }

    class AuthMiddleware {
        +validar_token(jwt: String) UsuarioSesion
        +verificar_rol_veterinario(usuario: UsuarioSesion) bool
    }

    class ServicioRegistroClinico {
        -repo_consulta: IRepositorioConsulta
        -repo_auditoria: IRepositorioAuditoria
        +corregir_entrada(consulta_id: String, dto: DTOEdicionConsulta, usuario_id: String) ResultadoEdicion
    }

    class ServicioAuditoria {
        -repo_auditoria: IRepositorioAuditoria
        +registrar_edicion(log: RegistroAuditoria)
        +registrar_rechazo(usuario_id: String, recurso: String)
    }

    class IRepositorioConsulta {
        <<interface>>
        +obtener_por_id(id: String) ConsultaClinica
        +guardar_version_atomica(version: VersionConsulta, audit: RegistroAuditoria) bool
    }

    class IRepositorioAuditoria {
        <<interface>>
        +guardar_log(log: RegistroAuditoria) bool
    }

    class RepositorioConsultaSQLAlchemy {
        -db_session: Session
        +obtener_por_id(id: String) ConsultaClinica
        +guardar_version_atomica(version: VersionConsulta, audit: RegistroAuditoria) bool
    }

    class Veterinario {
        +id: String
        +nombre: String
        +matricula: String
        +es_autor(autor_id: String) bool
    }

    class ConsultaClinica {
        +id: String
        +paciente_id: String
        +fecha_creacion: DateTime
        +version_activa_id: String
        +obtener_version_vigente() VersionConsulta
    }

    class VersionConsulta {
        +id: String
        +consulta_id: String
        +parent_version_id: String
        +numero_version: int
        +peso: float
        +sintomas: String
        +diagnostico: String
        +autor_id: String
        +motivo_edicion: String
        +fecha_registro: DateTime
        +validar_motivo() bool
    }

    class RegistroAuditoria {
        +id: String
        +fecha_hora: DateTime
        +usuario_id: String
        +accion: String
        +version_anterior_id: String
        +version_nueva_id: String
        +motivo: String
    }

    PantallaEdicionConsulta --> ControladorConsulta
    ControladorConsulta --> AuthMiddleware
    ControladorConsulta --> ServicioRegistroClinico
    ControladorConsulta ..> DTOEdicionConsulta
    
    ServicioRegistroClinico --> IRepositorioConsulta
    ServicioRegistroClinico --> IRepositorioAuditoria
    ServicioRegistroClinico --> ServicioAuditoria
    
    RepositorioConsultaSQLAlchemy ..|> IRepositorioConsulta
    
    ServicioRegistroClinico ..> Veterinario
    ServicioRegistroClinico ..> ConsultaClinica
    ServicioRegistroClinico ..> VersionConsulta
    ServicioRegistroClinico ..> RegistroAuditoria
    
    ConsultaClinica "1" *-- "1..*" VersionConsulta : historial_versiones
    VersionConsulta "0..1" --> "1" VersionConsulta : parent_version
```

---

### 4.2 Detalle de Clases, Interfaces y DTOs

1. **`PantallaEdicionConsulta` (UI / Boundary):** Formulario web que captura los cambios y preserva el estado en cliente si ocurre un fallo.
2. **`ControladorConsulta` (API Controller):** Recibe las solicitudes HTTP PUT, convierte los datos en DTOs e invoca la capa de servicio.
3. **`ServicioRegistroClinico` (Application Service):** Contiene la regla de orquestación de la edición de entradas clínicas.
4. **`VersionConsulta` (Domain Entity):** Representa el estado inmutable de una consulta en la versión $N$. Garantiza que `motivo_edicion` no esté vacío.
5. **`IRepositorioConsulta` (Puerto / Interfaz):** Abstrae la persistencia física, definiendo el contrato para guardados atómicos.
6. **`RepositorioConsultaSQLAlchemy` (Adaptador ORM):** Implementa el contrato SQL gestionando las transacciones ACID con `commit` y `rollback`.

---

## 5. Justificación del Diseño

### 5.1 Criterios GRASP Aplicados

- **Information Expert (Experto en Información):**
  - Asignado a `VersionConsulta` para validar sus propios atributos (`motivo_edicion`) y calcular el siguiente `numero_version`.
  - Asignado a `Veterinario` para validar la coincidencia de autoría entre el token y el registro.
- **Creator (Creador):**
  - `ServicioRegistroClinico` crea las instancias de `VersionConsulta` y `RegistroAuditoria` porque tiene los datos necesarios reunidos.
- **Controller (Controlador):**
  - `ControladorConsulta` actúa como primer punto de entrada no-UI para coordinar la ejecución del caso de uso.
- **Low Coupling (Bajo Acoplamiento):**
  - La capa de servicios depende de interfaces abstractas (`IRepositorioConsulta`), lo que permite intercambiar SQLAlchemy por repositorios en memoria durante los tests unitarios.
- **High Cohesion (Alta Cohesión):**
  - Las funciones de auditoría se delegan a `ServicioAuditoria`, evitando contaminar la clase de negocio con detalles del log.
- **Polymorphism / Indirection (Polimorfismo e Indirección):**
  - El uso de interfaces de repositorio desacopla el dominio de la infraestructura de base de datos relacional.

---

### 5.2 Decisiones Locales y Patrones de Diseño

1. **Patrón DTO (Data Transfer Object):** `DTOEdicionConsulta` desacopla la estructura JSON que envía el cliente web de los objetos del dominio.
2. **Patrón Append-Only Versioning:** Para responder a **EC-04 (DA-06)**, no se utiliza la sentencia SQL `UPDATE` sobre los datos clínicos de la consulta; únicamente se ejecutan `INSERT` de nuevas versiones.
3. **Patrón Unit of Work (vía ORM Session):** Garantiza que la escritura de la versión y el log de auditoría compartan la misma transacción atómica de base de datos (**EC-03 / DA-03**).

---

## 6. Coherencia y Trazabilidad

### 6.1 Tabla de Verificación de Coherencia

| Verificación | ¿Se cumple? | Evidencia en el Documento |
| :--- | :---: | :--- |
| **1. Cada participante de la secuencia pertenece a un componente C4** | **Sí** | `AuthMiddleware` $
ightarrow$ Auth/RBAC; `ControladorConsulta` $
ightarrow$ Controladores REST; `ServicioRegistroClinico` $
ightarrow$ Servicio Registro; `RepositorioORM` $
ightarrow$ Acceso a Datos. |
| **2. Mensajes inter-componentes existen en catálogo TP3** | **Sí** | `PUT /api/v1/consultas` (HTTPS/JSON); Invocación interna entre Servicios; `INSERT/SQL` hacia PostgreSQL. |
| **3. Respeta restricciones del estilo y patrones del TP3** | **Sí** | Respeta la arquitectura en **Capas** (las dependencias van solo hacia abajo, sin saltos) y el estilo **Repositorio**. |
| **4. Táctica de calidad aparece como operación explícita** | **Sí** | Táctica *Auditoría* y *Versionado Inmutable* en paso 7 de Secuencia A (`generar_log_edicion`) y paso 9 (`guardar_version_atomica`). |
| **5. Entidades del diagrama de robustez están en el modelo TP1** | **Sí** | `Veterinario`, `ConsultaClinica`, `VersionConsulta` y `RegistroAuditoria` figuran en el modelo del TP1 y Secc. 3.1. |
| **6. Medida del escenario se verifica con pruebas** | **Sí** | Medida de **EC-04** (100% de ediciones reconstruibles) verificada mediante pruebas unitarias e integración en Parte C. |

---

### 6.2 Matriz de Trazabilidad Completa

| Historia de Usuario | Escenario de Calidad | Decisión Arquitectura | Componente C4 (TP3) | Clases de Diseño (TP4) | Archivo de Código (src/) | Caso de Prueba (tests/) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **HU-02** (Edición de entrada) | **EC-04** (Responsabilidad) | **DA-06** (Append-Only) | `ServicioRegistroClinico` | `VersionConsulta`, `ServicioRegistroClinico` | `src/domain/version_consulta.py`, `src/services/registro_service.py` | `tests/test_versionado.py::test_crear_version_correcta` |
| **HU-02** (Edición de entrada) | **EC-02** (Integridad) | **DA-02** (RBAC Backend) | `AuthMiddleware` | `AuthMiddleware`, `Veterinario` | `src/middleware/auth.py` | `tests/test_auth.py::test_rechazo_usuario_no_autor` |
| **HU-02** (Edición de entrada) | **EC-03** (Recuperación) | **DA-03** (Transacciones) | `AccesoADatosORM` | `RepositorioConsultaSQLAlchemy` | `src/repositories/consulta_repository.py` | `tests/test_persistencia.py::test_rollback_por_error_auditoria` |
| **HU-02** (Edición de entrada) | **EC-01** (Operabilidad) | **DA-01** (Estado en UI) | `ModeloFormulario` | `PantallaEdicionConsulta`, `DTOEdicionConsulta` | `src/static/js/formulario_edicion.js` | `tests/test_ui.py::test_conservar_borrador_ante_error` |
