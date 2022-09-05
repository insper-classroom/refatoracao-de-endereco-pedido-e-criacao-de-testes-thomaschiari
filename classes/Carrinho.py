#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.itens = {}

    def adicionar_item(self, item:Produto, qtd=1):
        
        id = item.get_id()
        
        # Implemente a adição do item no dicionário
        if id in self.itens:
            self.itens[id] += qtd
        else:
            self.itens[id] = qtd


    def remover_item(self, item:Produto):
        pass
        # Implemente este método
    
    def get_itens(self):
        return self.itens

    def __str__(self):
        lista_itens = []
        for key, value in self.itens.items():
            lista_itens.append(f'Produto: {key} | Quantidade: {value}')
        return lista_itens

    def __repr__(self):
        return self.__str__()