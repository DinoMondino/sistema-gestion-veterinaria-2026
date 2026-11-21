# Sistema de gestión clínica veterinaria (Pequeños animales)
## Ingeniería de Software (2026)

## Integrantes
Mondino, Maria Delfina

Sarmiento, Augusto

Olivera Villa, Julieta

---
## 1. Propuesta de proyecto
Sistema para veterinarias que centraliza turnos, historia clínica, calendario de vacunación y registro de pagos, pensado para tres perfiles de uso (secretaria, veterinario/a y dueño de mascota), con consulta a la base OMIA como apoyo al diagnóstico veterinario sobre patologías hereditarias/genéticas.

---
## 2. Modelo de ciclo de vida
Se seleccionó un Modelo Incremental + Ágil: Permite entregar un núcleo administrativo y un MVP funcional rápido para validar con usuarios reales antes de incorporar módulos complejos.
Los requerimientos son razonablemente claros por rol (secretaria, veterinario, dueño), pero es esperable que se ajusten a medida que el grupo profundice en el dominio clínico y en la integración con OMIA, por eso conviene entregar y validar funcionalidad por incrementos en vez de esperar al sistema completo.
Se aíslan riesgos técnicos dejándolos para iteraciones posteriores y se implementarán reuniones breves e iteraciones controladas para acompañar la evolución dinámica de los requerimientos en el dominio veterinario.

---
* [Ver SRS: Canvas de descubrimiento](docs/requirements/srs.md)

* 
---

## 3. TP4 — Implementación de HU-01

Se implementó el registro de consultas veterinarias con validación de datos obligatorios, mensajes de error por campo y almacenamiento persistente en SQLite.

### Requisitos

- Python 3.10 o superior.
- Dependencias de `requirements.txt`.
- Para las pruebas, dependencias de `requirements-test.txt`.

### Instalación

Desde la carpeta principal del repositorio:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-test.txt
```

### Ejecutar la aplicación

```powershell
.\.venv\Scripts\python.exe app.py
```

Abrir en el navegador:

http://127.0.0.1:5000/

La base SQLite se crea automáticamente en `data/vetgestion.db`.

### Ejecutar las pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

### Generar cobertura

```powershell
.\.venv\Scripts\python.exe tests/test_hu01.py
```

Los resultados se generan en:

- `tests/cobertura/cobertura.txt`
- `tests/cobertura/html/index.html`

### Documentación del TP4

- [Diseño detallado](docs/design/diseno-detallado.md)
- [Implementación HU-01](docs/design/implementacion-hu01.md)
- [Pruebas y cobertura](tests/cobertura/cobertura.txt)

### Alcance

Este incremento implementa HU-01 del proceso Gestión Clínica e Historial.

La autenticación se encuentra simulada y no se implementan los demás módulos del sistema.

