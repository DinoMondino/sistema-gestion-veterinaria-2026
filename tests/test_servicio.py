"""ServicioRegistroClinico: coordina el alta solo si la validación es exitosa (RN-03)."""
import pytest

from datos_prueba import RepositorioCaido, RepositorioEspia, datos_validos, servicio_con
from src.infraestructura.repositorios import ErrorPersistencia, RepositorioClinicoEnMemoria


def test_rechaza_sin_guardar():
    """CP-26."""
    repo = RepositorioEspia()
    datos = datos_validos()
    datos.update(peso="-5", fecha="")
    resultado = servicio_con(repo).registrar(1, datos)
    assert resultado.estado == "invalido"
    assert set(resultado.errores) == {"fecha", "peso"}
    assert resultado.consulta is None
    assert repo.llamadas_guardar == 0          # ni siquiera se invoca la persistencia (RN-03)
    assert repo.listar_consultas(1) == []
    assert datos["sintomas"] == "Fiebre"       # la entrada no se altera


def test_guarda_consulta_valida():
    """CP-27."""
    repo = RepositorioEspia()
    resultado = servicio_con(repo).registrar(1, datos_validos())
    assert resultado.estado == "creado"
    assert resultado.errores == {}
    assert resultado.consulta.id == 1
    assert repo.llamadas_guardar == 1
    assert repo.listar_consultas(1) == [resultado.consulta]


def test_asocia_la_consulta_a_la_historia_de_la_mascota():
    """CP-28: la consulta de Toby (mascota 2) queda en su historia y con el veterinario de demostración."""
    repo = RepositorioClinicoEnMemoria()
    resultado = servicio_con(repo).registrar(2, datos_validos())
    assert resultado.consulta.historia_id == 2
    assert resultado.consulta.veterinario_id == 1
    assert repo.listar_consultas(1) == []


@pytest.mark.parametrize("datos", [
    pytest.param(datos_validos(), id="CP-29a-datos-validos"),
    pytest.param({}, id="CP-29b-datos-invalidos"),
])
def test_mascota_inexistente(datos):
    """CP-29: se informa 'no_encontrado' antes de validar y no se guarda nada."""
    repo = RepositorioEspia()
    resultado = servicio_con(repo).registrar(999, datos)
    assert resultado.estado == "no_encontrado"
    assert repo.llamadas_guardar == 0


def test_entrega_todos_los_errores_en_una_sola_respuesta():
    """CP-30 (EC-01): cuatro campos inválidos se informan juntos, sin ida y vuelta por campo."""
    resultado = servicio_con(RepositorioEspia()).registrar(1, {})
    assert resultado.estado == "invalido"
    assert set(resultado.errores) == {"fecha", "peso", "sintomas", "diagnostico"}


def test_una_falla_de_la_base_se_propaga_y_no_hay_exito_aparente():
    """CP-31 (EC-03): el servicio no oculta el error de persistencia."""
    with pytest.raises(ErrorPersistencia):
        servicio_con(RepositorioCaido()).registrar(1, datos_validos())
