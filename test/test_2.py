import pytest
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido

@pytest.mark.operacoes_carrinho
def test_carrinho():
    bombril = Produto('123456', 'Bombril')
    carrinho = Carrinho()
    carrinho.adicionar_item(bombril, 2)
    assert carrinho.itens[bombril.id] == 2

@pytest.mark.operacoes_pessoafisica
def test_pessoafisica():
    pessoa = PessoaFisica('12345678901', 'joaosilva@silva.top', 'Silva')
    assert pessoa.cpf == '12345678901'
    assert pessoa.email == 'joaosilva@silva.top'
    assert pessoa.nome == 'Silva'

@pytest.mark.operacoes_produto
def test_produto():
    produto = Produto('1234567890', 'Bombril')
    assert produto.id == '1234567890'
    assert produto.nome == 'Bombril'

@pytest.mark.operacoes_pedido
def test_pedido():
    bombril = Produto('123456', 'Bombril')
    carrinho = Carrinho()
    carrinho.adicionar_item(bombril, 2)
    pessoa = PessoaFisica('12345678901', 'joaosilva@silva.top', 'Silva')
    pedido = Pedido('Rua dos Bobos, 0', 'Rua dos Bobos, 0', pessoa, carrinho)
    assert pedido.endereco_entrega == 'Rua dos Bobos, 0'
    assert pedido.endereco_faturamento == 'Rua dos Bobos, 0'
    assert pedido.pessoa == pessoa
    assert pedido.carrinho == carrinho
    
