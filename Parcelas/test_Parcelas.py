import pytest
from Parcelas.Parcelas import Parcelas

@pytest.mark.parametrize(
    "tipo_actual,nuevo_tipo",
    [
        ('A','B'),
        ('B','C'),

    ]
)
def test_trasnformacion_suelo(tipo_actual, nuevo_tipo):
    p = Parcelas('P', tipo_actual, 5)
    p.transformacionSuelo(nuevo_tipo)
    assert p.tipo_suelo == nuevo_tipo