import pytest
from Archivos.Archivos import Archivos
from Parcelas.Parcelas import Parcelas


def test_guardar(tmpdir):
    a = Archivos()
    p = Parcelas('a','B', 5)
    data_in = 'a/B/5/\n'
    fpath = f"{tmpdir}/test.txt"

    a.guardar(ruta=fpath, diccionario={p.identificador: p})

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == data_out