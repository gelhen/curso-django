import pytest
from model_mommy import mommy

from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    modulos = Modulo.objects.all()
    return [mommy.make(Modulo, titulo=s) for s in modulos]

def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()

