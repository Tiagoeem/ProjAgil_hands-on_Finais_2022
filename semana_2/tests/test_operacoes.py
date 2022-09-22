from quadronegro import *
import pytest

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert  12 == soma(v1, v2)

@pytest.mark.op_simples
def test_soma_valor_positivo_e_negativo():
    v1 = 5
    v2 = -7
    assert  -2 == soma(v1, v2)

@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    v1 = 5
    v2 = 10
    assert  -5 == sub(v1, v2)

@pytest.mark.op_simples
def test_sub_valor_positivo_e_negativo():
    v1 = 5
    v2 = -10
    assert  15 == sub(v1, v2)

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    v1 = 5
    v2 = 10
    assert  50 == multiplicacao(v1, v2)

@pytest.mark.op_complexa
def test_media_de_uma_lista_numerica():
    assert  12.5 == media_lista_valores([10,30,5,5])
