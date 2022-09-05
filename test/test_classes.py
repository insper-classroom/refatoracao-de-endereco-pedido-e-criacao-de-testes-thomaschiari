import pytest
from classes.Endereco import Endereco
import requests

@pytest.mark.operacoes_cep
def test_cep_sem_internet():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep(Endereco, '13010061')

@pytest.mark.operacoes_cep
def test_cep_inteiro():
    cep = Endereco(13010061, 300)
    assert cep.rua == 'Rua Costa Aguiar'

@pytest.mark.operacoes_cep
def test_cep_string():
    cep = Endereco('13010061', 300)
    assert cep.rua == 'Rua Costa Aguiar'

@pytest.mark.operacoes_cep
def test_cep_digitos_a_mais():
    cep = Endereco.consultar_cep(Endereco, '130100611')
    assert cep == False

@pytest.mark.operacoes_cep
def test_cep_digitos_a_menos():
    cep = Endereco.consultar_cep(Endereco, '130611')
    assert cep == False

@pytest.mark.operacoes_cep
def test_cep_invalido():
    cep = Endereco.consultar_cep(Endereco, '00000000')
    assert cep == False

