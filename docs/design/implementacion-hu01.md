# TP4 — Parte B: Implementación de HU-01

**Alcance:** nueva consulta clínica; validación de fecha, peso, síntomas y diagnóstico; conservación de datos ante rechazo; registro correcto en repositorio en memoria y listado en pantalla.

## Recorrido

1. La interfaz (`templates/nueva_consulta.html`, `static/hu01.js`) conserva los campos del formulario y presenta errores.
2. El controlador REST (`src/api/controladores.py`) recibe y responde JSON.
3. El servicio (`src/aplicacion/servicio_registro.py`) coordina el caso de uso.
4. El validador (`src/aplicacion/validacion.py`) aplica RF-10 y genera los errores para RF-11.
5. Las entidades (`src/dominio/entidades.py`) representan Consulta, HistoriaClinica, Mascota y Veterinario.
6. El repositorio abstracto y el repositorio en memoria (`src/infraestructura/repositorios.py`) aíslan la persistencia.

## Demostración

- Abrir `/`. Seleccionar peso `-2` y borrar la fecha. Completar síntomas y diagnóstico; pulsar «Guardar Consulta». Se muestran errores bajo cada campo, con borde rojo, y se mantienen los datos.
- Corregir fecha y peso positivo y volver a guardar: la API responde con creación y la consulta aparece en la lista.
- Los datos se guardan en la base SQLite `data/vetgestion.db`, así que **persisten al reiniciar el proceso**. Para volver al estado inicial se borra el archivo y la aplicación lo recrea con `schema.sql`.

## Decisiones de alcance

- API Flask y frontend HTML/CSS/JavaScript separados, coherentes con las capas de la API y el MVC planteados en TP3.
- La autenticación es simulada con un veterinario fijo. No existe conexión con OMIA ni procesamiento de pagos.
- Se eligió **SQLite** como persistencia, detrás del puerto `RepositorioClinico` (clase `RepositorioClinicoSQL`). Es una simplificación respecto del TP3, que define PostgreSQL como base central (`DA-04`): cambiarla implica solo otra implementación del mismo puerto. Las pruebas usan SQLite en memoria.
- El código anterior del TP2 en `docs/ui/mockups/` queda sin cambios; esta es una implementación independiente en la raíz y `src/`.

## Contrato REST mínimo

| Método | Ruta | Respuesta |
|---|---|---|
| GET | `/api/mascotas/1` | 200 y contexto de la mascota |
| POST | `/api/mascotas/1/consultas` | 201 si se guarda; 422 y `errores` por campo si falla validación |
| GET | `/api/mascotas/1/consultas` | 200 y consultas guardadas en memoria |

El error de validación se devuelve en un único objeto JSON; el formulario no se borra en los rechazos.
