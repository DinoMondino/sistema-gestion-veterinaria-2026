# Documento de Diseño Detallado — TP4 (Parte A)
**Asignatura:** Ingeniería del Software 2026 — Trabajo Práctico 4  
**Proceso:** Gestión Clínica e Historial  
**Historia de Usuario:** HU-01 — Manejo de datos obligatorios incompletos o con formato inválido 

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
| **Calidad**       | EC-01: Operabilidad. Tácticas: mantener modelos de tarea, de usuario y del sistema; reducir sobrecarga. DA-02: interfaz MVC con conservación del formulario y devolución conjunta de errores por campo. EC-03                                                                                                                                                                                                        |
| **Dominio**       | Se utilizan Veterinario, Mascota, HistoriaClinica y Consulta para representar el profesional, el paciente, su historial y los datos de la consulta que se intenta registrar.                                                                                                                                                                                                                                    |
| **Verificación**  | Para la HU: ingresar peso negativo o fecha vacía y comprobar rechazo, mensaje específico, campo resaltado, ausencia de almacenamiento y conservación de datos. Para EC-01: comprobar 0 pérdidas de datos ante errores y medir el registro crítico en ≤ 45 segundos y ≤ 8 interacciones, con al menos 90 % de pruebas exitosas en las condiciones definidas por el escenario.                                    |

---

### 1.5 Entidades del Modelo de Dominio Intervinientes

Entidades del modelo de dominio del TP1 (`modelo_de_dominio_inicial.md`) analizadas para HU-01:

| Entidad del TP1 | ¿Interviene? | Qué utiliza la HU de ella | La HU la... |
|---|---|---|---|
| **Usuario** | Indirectamente | Identidad y rol del usuario autenticado, mediante `Veterinario` | Consulta |
| **Secretaria** | No | No participa en el registro clínico de esta HU | — |
| **Veterinario** | Sí | Profesional que intenta registrar la consulta | Consulta |
| **DuenioMascota** | No | Los datos del tutor no intervienen en la validación | — |
| **Mascota** | Sí | Identificación del paciente al que corresponde la consulta | Consulta |
| **HistoriaClinica** | Sí | Historial al que se asociaría la consulta | Consulta (no la modifica) |
| **Consulta** | Sí | Fecha y demás datos clínicos, incluido el peso que debe validarse | Intenta crearla (si hay errores, el guardado se rechaza) |
| **Vacuna** | No | No se validan vacunas en este escenario | — |
| **AplicacionVacuna** | No | No se registra una aplicación de vacuna | — |
| **Turno** | No | No se gestiona la agenda | — |
| **Prescripcion** | No | No se registra una prescripción | — |
| **ReaccionAdversaRegistrada** | No | No se registra una reacción adversa | — |
| **Pago** | No | No corresponde al proceso de validación clínica | — |
| **PatologiaReferencia** | No | No se realiza una consulta a OMIA | — |

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



## 2.1 Diagrama de Robustez

```mermaid

flowchart TB
    vet["Médico Veterinario<br/>(actor)"]

    ui(["«boundary»<br/>FormularioNuevaConsulta"])
    cp(("«controller»<br/>ControladorPantalla"))
    api(["«boundary»<br/>ServicioRegistroClinico"])
    repo(("«controller»<br/>RepositorioClinico"))

    mascota[["«entity»<br/>Mascota"]]
    historia[["«entity»<br/>HistoriaClinica"]]
    consulta[["«entity»<br/>Consulta"]]

    vet --> ui
    ui <--> cp
    cp <--> api
    api <--> repo

    repo --> mascota
    repo --> historia
    repo --> consulta

    mascota -.->|"tiene 1 historia"| historia
    historia -.->|"contiene 0..* consultas"| consulta

    classDef actor fill:#f3f4f6,stroke:#4b5563,color:#111827,stroke-dasharray:4 3
    classDef boundary fill:#dbeafe,stroke:#1d4ed8,color:#0f172a
    classDef controller fill:#ffedd5,stroke:#c2410c,color:#0f172a
    classDef entity fill:#dcfce7,stroke:#15803d,color:#0f172a

    class vet actor
    class ui,api boundary
    class cp,repo controller
    class mascota,historia,consulta entity

```



---

### 2.2 Ubicación de Reglas de Negocio

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
| **ServicioRegistroClinico**     | `API clínica: Controladores REST registro clínico y Validación `                  | Boundary — API clínica, representación simplificada|
| **RepositorioClinico** | `Acceso a datos`; se comunica con el contenedor **Base de datos central** por **SQL** (relación "Lee y escribe" del catálogo 7.1.3 del TP3) | Datos e integración — API clínica |
| **Consulta** | `Servicio de registro clínico` la crea; `Acceso a datos` la guarda (tabla `consulta`) | Entidad de dominio creada y almacenada |
| **Mascota** | `Acceso a datos` (tabla `mascota` en la Base de datos central) | Entidad de dominio |
| **HistoriaClinica** | `Acceso a datos` (tabla `historia_clinica`) | Entidad de dominio |
---

## Paso 4 — Diagramas de Secuencia y Asignación de Responsabilidades

### Contexto y Convenciones

* **Secuencia A: Camino Principal.** El veterinario ya corrigió y guarda con datos válidos (CU-01, pasos 5 a 7). Es el destino de la HU: «corregirlos» y poder guardar.
* **Secuencia B: Caminos de Rechazo.** Es el camino que pide el criterio de aceptación: peso negativo y/o fecha en blanco. Las dos causas son variantes pequeñas del mismo camino (se muestran con `opt`) y se informan juntas.
* **Seguridad (EC-02):** El rechazo por falta de permisos pertenece a EC-02 y RF-08, no es criterio de HU-01: en las dos secuencias se modela solo el caso habilitado.
* **Convenciones:** La flecha punteada con cruz (`--x`) es un error que el servicio señala; los mensajes entre componentes siguen el catálogo del TP3. `Modelo de formulario` y `Cliente de la API` se tratan como colaboradores internos de `ControladorPantalla`, tal como dice la tabla de correspondencia del Paso 3.

---

### 4.1 Secuencia A: Camino Principal (Flujo Exitoso)

```mermaid
sequenceDiagram
    actor Vet as Médico Veterinario
    participant UI as FormularioNuevaConsulta
    participant CP as ControladorPantalla
    participant REST as ControladorREST
    participant SRC as ServicioRegistroClinico
    participant RC as RepositorioClinico
    participant VAL as ValidacionRegistrosClinicos
    participant C as Consulta
    participant BD as Base de datos central

    Vet->>UI: Presiona Guardar Consulta
    UI->>CP: enviar datos del formulario
    CP->>REST: POST /api/mascotas/1/consultas

    REST->>SRC: registrar(mascota_id, datos)
    SRC->>RC: obtener_contexto(mascota_id)
    RC->>BD: SELECT mascota e historia clínica
    BD-->>RC: filas
    RC-->>SRC: mascota e historia clínica

    SRC->>VAL: validar(datos)
    VAL-->>SRC: datos válidos, sin errores

    SRC->>C: crear Consulta
    SRC->>RC: guardar_consulta(consulta)
    Note over RC,BD: Una sola transacción: se guarda completa o no se guarda (EC-03)
    RC->>BD: BEGIN + INSERT INTO consulta
    BD-->>RC: id asignado
    RC->>BD: COMMIT
    RC-->>SRC: consulta guardada con id

    SRC-->>REST: registro exitoso
    REST-->>CP: HTTP 201
    CP->>UI: mostrar confirmación
    UI-->>Vet: Consulta registrada
```

---

### 4.2 Secuencia B: Caminos de Rechazo (Datos Inválidos)


```mermaid
sequenceDiagram
    actor Vet as Médico Veterinario
    participant UI as FormularioNuevaConsulta
    participant CP as ControladorPantalla
    participant REST as ControladorREST
    participant SRC as ServicioRegistroClinico
    participant RC as RepositorioClinico
    participant VAL as ValidacionRegistrosClinicos
    participant BD as Base de datos central

    Vet->>UI: Presiona Guardar Consulta
    UI->>CP: enviar datos del formulario
    Note over UI,CP: Se conservan los valores ingresados
    CP->>REST: POST /api/mascotas/1/consultas

    REST->>SRC: registrar(mascota_id, datos)
    SRC->>RC: obtener_contexto(mascota_id)
    RC->>BD: SELECT mascota e historia clínica
    BD-->>RC: filas
    RC-->>SRC: mascota e historia clínica

    SRC->>VAL: validar(datos)
    VAL-->>SRC: errores por campo

    Note over SRC,BD: No se crea la consulta ni se llama a guardar_consulta: no hay INSERT, 0 registros guardados
    SRC-->>REST: registro rechazado, errores
    REST-->>CP: HTTP 422, errores
    CP->>UI: mostrar errores por campo
    UI-->>Vet: Resalta errores y conserva los datos
```

---

## 4.2.1 Secuencia C: falla de la base al guardar

Cubre la táctica de transacciones y rollback de EC-03 (`DA-04`, `DA-05`). No la exige el criterio de aceptación de HU-01.

```mermaid
sequenceDiagram
    actor Vet as Médico Veterinario
    participant UI as FormularioNuevaConsulta
    participant CP as ControladorPantalla
    participant REST as ControladorREST
    participant SRC as ServicioRegistroClinico
    participant RC as RepositorioClinico
    participant BD as Base de datos central
    participant EXC as GestionExcepciones

    CP->>REST: POST /api/mascotas/1/consultas
    REST->>SRC: registrar(mascota_id, datos válidos)
    SRC->>RC: guardar_consulta(consulta)
    RC->>BD: BEGIN + INSERT INTO consulta
    BD--xRC: error de la base
    RC->>BD: ROLLBACK
    RC--xSRC: error de persistencia
    SRC--xREST: propaga el error
    REST->>EXC: traducir(error)
    EXC-->>REST: respuesta controlada
    REST-->>CP: HTTP 503, aviso de mantenimiento
    CP->>UI: mostrar aviso y conservar lo cargado
    UI-->>Vet: No se guardó; los datos siguen en pantalla
```

---

### 4.3 Demostración de la Táctica de Calidad (EC-01 / DA-02)

| Táctica | Operación o mensaje que la muestra | Evidencia en el diseño |
| :--- | :--- | :--- |
| **Mantener modelos de tarea, de usuario y del sistema** (`Modelo de formulario`) | `conservar_datos(campos)` **antes** de enviar y `registrar_errores(errores)` al volver el rechazo | La pantalla se redibuja desde ese estado (`mostrar_errores(errores, campos)`) $\rightarrow$ **0 pérdidas de datos**. |
| **Reducir sobrecarga** (`ValidacionRegistrosClinicos`) | Una sola llamada `validar(datos)` recorre todos los campos y devuelve **todos** los errores juntos en un único `DatosInvalidosError` | Menos interacciones ida y vuelta entre cliente y servidor. |
| **Transacciones y rollback** (EC-03, `DA-04`) | `BEGIN` / `COMMIT` en `guardar_consulta`; `ROLLBACK` si falla el `INSERT` (Secuencia C) | Una consulta se guarda completa o no se guarda: no quedan registros parciales. |

---

### 4.4 Asignación de Responsabilidades (Criterios GRASP)

| Responsabilidad | Quién | Criterio GRASP | Por qué |
| :--- | :--- | :--- | :--- |
| **Captar los datos y mostrar errores resaltados o la confirmación** | `FormularioNuevaConsulta` | Bajo acoplamiento | Solo conoce al controlador de pantalla. No decide qué es inválido: resalta lo que le informan. |
| **Conservar lo ingresado y los errores, y coordinar el envío** | `ControladorPantalla` | Controlador | Recibe el evento de la pantalla y lo coordina; es el Modelo de formulario de `EC-01`. |
| **Interpretar el pedido (JSON $\rightarrow$ `DatosConsulta`) y armar la respuesta** | `ControladorREST` | Controlador | Es la entrada de la API clínica (capa Presentación). |
| **Identificar al usuario y verificar que puede registrar consultas** | `AutenticacionAutorizacion` | Creador | Tiene los datos del token para crear el `Veterinario`. |
| **Saber si el veterinario puede registrar consultas** | `Veterinario` | Experto en información | Conoce su rol. |
| **Coordinar el registro: validar, obtener la historia, registrar, guardar** | `ServicioRegistroClinico` | Controlador (del caso de uso) | Ordena los pasos; no valida ni decide reglas del dominio. Impide guardar si hay errores (RN-03). |
| **Recorrer todos los campos y juntar los errores por campo** | `ValidacionRegistrosClinicos` | Alta cohesión | Su única tarea es aplicar las reglas de RF-10 y armar los errores de RF-11 (RN-04); la reutiliza también el servicio de prescripciones (TP3). |
| **Decidir si una fecha y un peso son válidos** | `Consulta` | Experto en información | Sabe qué es una fecha de atención y un peso admisibles (RN-01, RN-02). |
| **Crear los errores y saber si hay alguno** | `ValidacionRegistrosClinicos` (crea) y `ErroresPorCampo` (`hay_errores`) | Creador y Experto | La validación los usa de forma directa; el contenedor conoce su contenido. |
| **Traducir el error en una respuesta controlada** | `GestionExcepciones` | Alta cohesión | Es el aspecto transversal del TP3; los servicios solo señalan. |
| **Obtener y guardar la mascota con su historia** | `RepositorioMascotas` | Alta cohesión y bajo acoplamiento | El servicio no sabe cómo se guarda. |
| **Saber cuál es su historia clínica** | `Mascota` | Experto en información | Tiene la relación 1 a 1 con su historia. |
| **Crear la consulta y agregarla a su historial** | `HistoriaClinica` | Creador | Contiene y «registra» consultas (modelo del TP1). |

---

## Paso 5 — Modelo de Clases (HU-01)

### Modelo de Clases Derivado de las Secuencias

```mermaid
classDiagram
    direction TB

    class ServicioRegistroClinico {
        +repositorio: RepositorioClinico
        +validador: ValidacionRegistrosClinicos
        +registrar(mascota_id, datos) ResultadoRegistro
    }

    class ValidacionRegistrosClinicos {
        +validar(datos) tuple
    }

    class ResultadoRegistro {
        +estado: str
        +errores: dict
        +consulta: Consulta
    }

    class RepositorioClinico {
        <<abstract>>
        +obtener_contexto(mascota_id)*
        +guardar_consulta(consulta)*
        +listar_consultas(historia_id)*
    }

    class RepositorioClinicoEnMemoria {
        -_lock: Lock
        +mascotas: dict
        +historias: dict
        +veterinario_demo: Veterinario
        -_consultas: list
        -_siguiente_id: int
        +obtener_contexto(mascota_id)
        +guardar_consulta(consulta)
        +listar_consultas(historia_id)
    }

    class Consulta {
        +id: int
        +historia_id: int
        +veterinario_id: int
        +fecha: date
        +peso: Decimal
        +sintomas: str
        +diagnostico: str
        +observaciones: str
    }

    class Mascota {
        +id: int
        +nombre: str
        +especie: str
        +peso_actual: Decimal
    }

    class HistoriaClinica {
        +id: int
        +mascota_id: int
    }

    class Veterinario {
        +id: int
        +nombre: str
    }

    ServicioRegistroClinico --> RepositorioClinico : utiliza
    ServicioRegistroClinico --> ValidacionRegistrosClinicos : utiliza
    ServicioRegistroClinico ..> ResultadoRegistro : crea
    ServicioRegistroClinico ..> Consulta : crea

    ResultadoRegistro --> Consulta : resultado opcional

    RepositorioClinicoEnMemoria --|> RepositorioClinico

    RepositorioClinicoEnMemoria --> Mascota : almacena
    RepositorioClinicoEnMemoria --> HistoriaClinica : almacena
    RepositorioClinicoEnMemoria --> Veterinario : demostracion
    RepositorioClinicoEnMemoria --> Consulta : almacena

```
## 6. IMPLEMENTACIÓN

### 6.1 Persistencia y datos iniciales

La persistencia usa **SQLite** detrás de la interfaz `RepositorioClinico`, mediante la clase `RepositorioClinicoSQL`. La base se crea con el script `schema.sql`, que define las tablas y carga los datos de demostración (antes estaban fijos en el constructor del repositorio en memoria):

| Tabla | Contenido inicial |
|---|---|
| `veterinario` | 1 — Dra. Ana Ríos (profesional fijo de demostración, la autenticación está simulada) |
| `mascota` | 1 — Luna (Perro, 6.8 kg); 2 — Toby (Gato, 4.1 kg) |
| `historia_clinica` | Una por mascota (1 → Luna, 2 → Toby) |
| `consulta` | Vacía: la completa la HU |

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE veterinario (
    id     INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE mascota (
    id          INTEGER PRIMARY KEY,
    nombre      TEXT NOT NULL,
    especie     TEXT NOT NULL,
    peso_actual TEXT NOT NULL
);

CREATE TABLE historia_clinica (
    id         INTEGER PRIMARY KEY,
    mascota_id INTEGER NOT NULL UNIQUE REFERENCES mascota(id)
);

CREATE TABLE consulta (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    historia_id    INTEGER NOT NULL REFERENCES historia_clinica(id),
    veterinario_id INTEGER NOT NULL REFERENCES veterinario(id),
    fecha          TEXT NOT NULL,
    peso           TEXT NOT NULL,
    sintomas       TEXT NOT NULL,
    diagnostico    TEXT NOT NULL,
    observaciones  TEXT NOT NULL DEFAULT ''
);

INSERT INTO veterinario VALUES (1, 'Dra. Ana Ríos');
INSERT INTO mascota VALUES (1, 'Luna', 'Perro', '6.8'), (2, 'Toby', 'Gato', '4.1');
INSERT INTO historia_clinica VALUES (1, 1), (2, 2);
```

La relación 1 a 1 entre `Mascota` e `HistoriaClinica` del modelo de dominio se refleja con `UNIQUE` en `mascota_id`. Las reglas de validación (RN-01 a RN-04) **siguen viviendo solo en `ValidacionRegistrosClinicos`**: la base no las duplica. El `id` de la consulta lo asigna la base (autoincremental), ya no el repositorio.

### 6.2 Mapeo de tipos y relación con la arquitectura

| Atributo del dominio | Tipo en Python | SQLite (TP4) | PostgreSQL (TP3, `DA-04`) |
|---|---|---|---|
| `id` | `int` | `INTEGER` (autoincremental) | `INTEGER` / identidad |
| `nombre`, `especie`, `sintomas`, `diagnostico`, `observaciones` | `str` | `TEXT` | `TEXT` / `VARCHAR` |
| `fecha` | `date` | `TEXT` (ISO 8601, `AAAA-MM-DD`) | `DATE` |
| `peso`, `peso_actual` | `Decimal` | `TEXT` | `NUMERIC(6,2)` |

El peso se guarda como `TEXT` en SQLite porque su tipo `NUMERIC` lo convertiría a punto flotante y se perdería la exactitud decimal que el dominio usa (`Decimal`). `RepositorioClinicoSQL` convierte al leer (`date.fromisoformat`, `Decimal(texto)`) y al escribir (`isoformat()`, `str`), de modo que servicio, validador y entidades siguen trabajando con `date` y `Decimal`.

**Simplificación respecto del TP3:** la arquitectura (`DA-04`) define PostgreSQL como "Base de datos central". En el TP4 se usa SQLite porque la consigna deja libre la elección de la base y no exige PostgreSQL; no requiere instalar ni configurar un servidor. Como el acceso está detrás de `RepositorioClinico`, pasar a PostgreSQL implica solo escribir otra implementación de esa interfaz (más el cambio de tipos de la tabla anterior), sin tocar el servicio ni el controlador.

## 7. Testing (HU-01)

## 8. Trazabilidad (HU-01)