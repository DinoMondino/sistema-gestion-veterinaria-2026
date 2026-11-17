# TP4 — Parte C: pruebas unitarias de HU-01

## Alcance

Pruebas unitarias de `ValidacionRegistrosClinicos.validar`, `ServicioRegistroClinico.registrar` y `RepositorioClinicoEnMemoria`, sin interfaz gráfica. La conservación de valores en los casilleros tras recibir HTTP 422 es responsabilidad de JavaScript; no se midió con estas pruebas de Python. La ausencia de guardado ante errores sí está verificada.

## Tabla de casos de prueba

| Caso | Técnica | Origen | Datos de entrada y estado | Resultado esperado |
|---|---|---|---|---|
| CP-01 | Caja negra (equivalencia) | HU-01: fecha obligatoria | Fecha vacía; demás campos válidos | Error específico en fecha |
| CP-02 | Caja negra (equivalencia) | HU-01: formato | Fecha imposible `2026-02-31` | Error en fecha |
| CP-03 | Caja negra (límite) | RF-10: fecha futura | Mañana; demás campos válidos | Rechazo de fecha posterior a hoy |
| CP-04 | Caja negra (equivalencia) | HU-01: peso inválido | Peso `-5` | Error específico en peso |
| CP-05 | Caja negra (valor límite) | HU-01: peso inválido | Peso `0` | Error en peso |
| CP-06 | Caja negra (equivalencia) | RF-10: formato | Peso `texto` | Error en peso |
| CP-07 | Caja blanca | `validar()`: peso no finito | Peso `NaN` | Error en peso |
| CP-08 | Caja negra (equivalencia) | RF-10: obligatoriedad | Síntomas vacíos | Error en síntomas |
| CP-09 | Caja negra (equivalencia) | RF-10: obligatoriedad | Diagnóstico vacío | Error en diagnóstico |
| CP-10 | Caja negra (equivalencia) | HU-01, RF-11 | Fecha vacía y peso `-5` | Devuelve los dos errores juntos |
| CP-11 | Caja negra (valor límite) | RF-10: dato positivo | Peso `0,01`; datos válidos | Sin errores y datos normalizados |
| CP-12 | Caja blanca | `validar()`: campo opcional | Sin clave observaciones | Se normaliza a texto vacío |
| CP-13 | Caja blanca | HU-01, EC-01, `registrar()` | Mascota 1; fecha vacía y peso `-5` | Resultado inválido, entrada inalterada, ninguna consulta guardada |
| CP-14 | Caja blanca | `registrar()`: éxito | Mascota 1; todos los datos válidos | Consulta creada y almacenada |
| CP-15 | Caja blanca | `registrar()`: contexto ausente | Mascota 999 | Resultado no encontrado, sin guardado |
| CP-16 | Caja blanca | `obtener_contexto()` | Mascota 1 y mascota 999 | Historia relacionada para 1, `None` para 999 |
| CP-17 | Caja blanca | `listar_consultas()` | Guardar una consulta en cada una de dos historias | Cada historial devuelve solo sus consultas e IDs diferentes |

## Trazabilidad y pruebas

| **Criterio / escenario** | **Caso de prueba** | **Prueba** |
|---|---|---|
| HU-01, fecha vacía | `CP-01` | `test_rechaza_campos_invalidos[CP-01]` |
| HU-01, fecha inválida | `CP-02`, `CP-03` | `test_rechaza_campos_invalidos[CP-02]`, `test_rechaza_campos_invalidos[CP-03]` |
| HU-01, peso negativo | `CP-04` | `test_rechaza_campos_invalidos[CP-04]` |
| HU-01, límite de peso | `CP-05`, `CP-11` | `test_rechaza_campos_invalidos[CP-05]`, `test_admite_valores_limite_validos_y_normaliza` |
| HU-01, peso mal formado | `CP-06`, `CP-07` | `test_rechaza_campos_invalidos[CP-06]`, `test_rechaza_campos_invalidos[CP-07]` |
| RF-10, campos obligatorios | `CP-08`, `CP-09` | `test_rechaza_campos_invalidos[CP-08]`, `test_rechaza_campos_invalidos[CP-09]` |
| RF-11, errores por campo | `CP-10` | `test_rechaza_varios_campos_en_un_solo_intento` |
| RF-10, observaciones opcionales | `CP-12` | `test_observaciones_opcionales` |
| HU-01 / EC-01, rechazo sin pérdida de entrada ni persistencia | `CP-13` | `test_servicio_rechaza_sin_guardar` |
| Registro válido | `CP-14` | `test_servicio_guarda_consulta_valida` |
| Contexto no encontrado | `CP-15` | `test_servicio_mascota_inexistente` |
| Contexto de mascota e historia | `CP-16` | `test_repositorio_mascota_y_historia_relacionadas` |
| Persistencia separada por historial | `CP-17` | `test_repositorio_consultas_separadas_por_historia` |

## Complejidad ciclomática de las operaciones de la HU

Conteo didáctico solicitado: **cantidad de decisiones (`if`, `for`, expresiones condicionales) + 1**. Los bloques `try/except` y los cortocircuitos booleanos añaden rutas de ejecución que se ejercitan con los casos correspondientes, aunque no se cuentan como decisiones adicionales en esta tabla simplificada. La métrica puede ser mayor si se utiliza una herramienta con una convención distinta.

| **Operación** | **Decisiones** | **Complejidad** | **Pruebas, una por camino** |
|---|---|---|---|
| `ValidacionRegistrosClinicos.validar` | 5: fecha vacía, fecha futura, peso fuera de rango, iteración de campos obligatorios, campo vacío | 6 | `CP-01` (fecha vacía), `CP-02` (fecha mal formada), `CP-03` (fecha futura), `CP-04`/`CP-05`/`CP-07` (peso inválido), `CP-08`/`CP-09` (campo vacío), `CP-11` (válido), `CP-12` (opcional), `CP-10` (errores simultáneos) |
| `ServicioRegistroClinico.registrar` | 2: contexto inexistente, errores de validación | 3 | `CP-15` (no encontrado), `CP-13` (inválido), `CP-14` (válido) |
| `RepositorioClinicoEnMemoria.obtener_contexto` | 1: presencia de mascota e historia | 2 | `CP-16` (encontrado y no encontrado) |
| `RepositorioClinicoEnMemoria.guardar_consulta` | 0 | 1 | `CP-14` (guardado) |
| `RepositorioClinicoEnMemoria.listar_consultas` | 1: filtrar por `historia_id` | 2 | `CP-13` (sin consultas), `CP-17` (coincidencias y exclusiones) |

## Reporte de cobertura obtenido

Ejecución real con Python 3.13.5, pytest 9.0.2, pytest-cov 7.0.0 y coverage 7.13.3:

```text
Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
src/aplicacion/servicio_registro.py      24      0      4      0   100%
src/aplicacion/validacion.py             31      0     10      0   100%
src/infraestructura/repositorios.py      32      0      0      0   100%
---------------------------------------------------------------------------------
TOTAL                                    87      0     14      0   100%
17 passed
```

**Análisis:** No quedaron líneas ni ramas sin cubrir en los tres módulos elegidos. El conjunto inicial ya alcanzó cobertura completa; por lo tanto, no fue necesario agregar casos después de analizar el reporte. Se incluyeron desde el principio casos de rechazo, éxito, límites, formatos y contexto inexistente. Una cobertura de 100 % no garantiza ausencia de defectos: por ejemplo, la prueba de rechazo del servicio comprueba que el diccionario de entrada sigue intacto, **pero no comprueba que el navegador conserve visualmente los casilleros** tras recibir el error. Tampoco cubre rutas REST en `src/api/controladores.py` ni `app.py`, ya que esas pertenecen a la capa HTTP y requieren Flask instalado. La medida completa de EC-01 (tiempo e interacciones) no fue evaluada por estas pruebas unitarias; aquí se verifica solo la conservación de entrada y el rechazo sin persistencia.

## Ejecución desde la raíz del repositorio

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-test.txt
.\.venv\Scripts\python.exe -m pytest -v tests/
.\.venv\Scripts\python.exe -m pytest tests/ --cov=src.aplicacion.validacion --cov=src.aplicacion.servicio_registro --cov=src.infraestructura.repositorios --cov-branch --cov-report=term-missing --cov-report=html
```

Abrir `htmlcov/index.html` para el reporte HTML. No subir `.venv/`, `.coverage`, `htmlcov/` ni `__pycache__/` al repositorio. Los resultados pueden variar si el código se modifica después de esta entrega.
