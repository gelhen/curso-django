import pytest
from django.urls import reverse
from model_mommy import mommy
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)

'''
Criar aulas respectivas ao modulo na fixture de cima "modulo"
Conetar o atributo modulo da aula ao objeto modulo criado na fixture modulo=modulo
'''
@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)

@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp

def test_titulo(resp, aula:Modulo):
    assert_contains(resp, aula.titulo)
