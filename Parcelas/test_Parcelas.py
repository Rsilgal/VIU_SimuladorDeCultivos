import pytest
from Parcelas.Parcelas import Parcelas

@pytest.mark.parametrize(
    "tipoActual,nuevoTipo",
    [
        ('A','B'),
        ('B','C'),

    ]
)
def test_trasnformacion_suelo(tipoActual, nuevoTipo):
    p = Parcelas('P', tipoActual, 5)
    p.transformacionSuelo(nuevoTipo)
    assert p.tipoSuelo == nuevoTipo