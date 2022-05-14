import pytest
from Cultivos.Cultivos import Cultivos


@pytest.mark.parametrize(
    "duracionInicial,factor,expected",
    [
        (15, 1, 14),
        (16, 5, 11),
        (1, 1, 0)
    ]
)
def test_dias_trasncurridos(duracion_inicial, factor, expected):
    cultivo = Cultivos('a','A',5,False,'B', duracion_inicial)
    cultivo.diasTranscurridos(factorDecremento=factor)
    assert cultivo.duracionCultivo == expected
