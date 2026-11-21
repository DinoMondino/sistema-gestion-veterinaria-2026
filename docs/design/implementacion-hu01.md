
# TP4 — Parte B: Implementación de HU-01

## 1. Alcance

Se implementó el registro de una nueva consulta veterinaria, con validación de fecha, peso, síntomas y diagnóstico.

Si los datos son inválidos, el sistema identifica los campos con errores, informa sus motivos y conserva los valores ingresados.

Si los datos son válidos, la consulta se guarda en SQLite y se incorpora al historial de la mascota.

## 2. Componentes implementados

| Componente | Archivo | Responsabilidad |
|---|---|---|
| FormularioNuevaConsulta | `templates/nueva_consulta.html` | Presentar el formulario |
| ControladorPantalla | `static/hu01.js` | Enviar datos, presentar errores y actualizar la pantalla |
| Controlador REST | `src/api/controladores.py` | Recibir solicitudes HTTP y devolver respuestas JSON |
| ServicioRegistroClinico | `src/aplicacion/servicio_registro.py` | Coordinar el registro |
| ValidacionRegistrosClinicos | `src/aplicacion/validacion.py` | Validar los datos clínicos |
| RepositorioClinico | `src/infraestructura/repositorios.py` | Definir las operaciones de persistencia |
| RepositorioClinicoSQLite | `src/infraestructura/repositorios.py` | Guardar y consultar datos en SQLite |
| Entidades del dominio | `src/dominio/entidades.py` | Representar Mascota, HistoriaClinica, Consulta y Veterinario |

## 3. Persistencia

Se utiliza SQLite, con la base ubicada por defecto en `data/vetgestion.db`.

El esquema se define en la constante `_ESQUEMA` de `src/infraestructura/repositorios.py` y se crea automáticamente al iniciar la aplicación.

La operación `guardar_consulta` almacena la consulta y actualiza el peso vigente de la mascota cuando corresponde, dentro de una misma transacción.

Los datos permanecen guardados después de reiniciar la aplicación.

También existe `RepositorioClinicoEnMemoria`, utilizado como alternativa durante las pruebas.

## 4. Respuestas de la API

| Método | Ruta | Resultado |
|---|---|---|
| GET | `/api/mascotas/1` | 200: información de la mascota |
| POST | `/api/mascotas/1/consultas` | 201: consulta guardada |
| POST | `/api/mascotas/1/consultas` | 422: errores de validación |
| POST | `/api/mascotas/1/consultas` | 400: cuerpo JSON inválido |
| POST | `/api/mascotas/999/consultas` | 404: mascota inexistente |
| POST | `/api/mascotas/1/consultas` | 503: error de persistencia |
| GET | `/api/mascotas/1/consultas` | 200: listado de consultas |

## 5. Demostración

1. Ejecutar `python app.py`.
2. Abrir `http://127.0.0.1:5000/`.
3. Ingresar peso negativo y borrar la fecha.
4. Presionar Guardar Consulta.
5. Comprobar que aparecen los errores, no se guarda la consulta y se conservan los valores.
6. Corregir los campos y guardar nuevamente.
7. Comprobar que la consulta aparece en el listado y se actualiza el peso vigente.
8. Reiniciar la aplicación y verificar que la consulta permanece guardada.

## 6. Decisiones de alcance

- La autenticación es simulada con un veterinario de demostración.
- No se implementan OMIA, pagos ni otros módulos ajenos a HU-01.
- SQLite reemplaza a PostgreSQL únicamente en el incremento implementado para TP4.
- La base se mantiene detrás de `RepositorioClinico`, de modo que puede sustituirse su implementación sin modificar el servicio de registro.
- El maquetado original del TP2 se mantiene separado en `docs/ui/mockups/`.
