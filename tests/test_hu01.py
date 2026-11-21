"""Ejecuta TODAS las pruebas de HU-01 y genera el reporte de cobertura dentro de tests/.

Uso, desde la raíz del proyecto:

    python tests/test_hu01.py

Genera:
    tests/cobertura/cobertura.txt   reporte de líneas y ramas, con las líneas no cubiertas
    tests/cobertura/html/index.html reporte navegable (abrir en el navegador)

Este archivo no define pruebas: las pruebas están en test_validacion.py, test_servicio.py,
test_repositorios.py y test_api.py. Con `python -m pytest` también se corren todas, sin cobertura.
"""
import os
import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
RAIZ = CARPETA.parent
SALIDA = CARPETA / "cobertura"


def main() -> int:
    try:
        import coverage
        import pytest
        import pytest_cov  # noqa: F401  (comprueba que el plugin está instalado)
    except ImportError:
        print("Faltan dependencias. Ejecutar: pip install -r requirements.txt")
        return 2

    os.chdir(RAIZ)
    sys.path.insert(0, str(RAIZ))
    SALIDA.mkdir(exist_ok=True)
    archivo_datos = SALIDA / ".coverage"
    os.environ["COVERAGE_FILE"] = str(archivo_datos)

    codigo = pytest.main([
        str(CARPETA), "-v", "-p", "no:cacheprovider",
        "--cov=src", "--cov=app", "--cov-branch",
        "--cov-report=term-missing",
        f"--cov-report=html:{SALIDA / 'html'}",
    ])

    cov = coverage.Coverage(data_file=str(archivo_datos), branch=True)
    cov.load()
    with open(SALIDA / "cobertura.txt", "w", encoding="utf-8") as salida:
        cov.report(file=salida, show_missing=True)
    print(f"\nReporte de texto: {SALIDA / 'cobertura.txt'}")
    print(f"Reporte HTML:     {SALIDA / 'html' / 'index.html'}")
    return int(codigo)


if __name__ == "__main__":
    sys.exit(main())
