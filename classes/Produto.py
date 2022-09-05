#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    produtos = {}

    def __init__(self, id_produto, nome=''):
        self.id = id_produto
        self.nome = nome
        Produto.produtos[self.nome] = self

    def set_id(self, id_nome):
        self.id = id_nome
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        return f'{self.id} - {self.nome}'

'''    def busca_nome(nome):
        produtos = []
        for produto in Produto.produtos.keys():
            if nome in produto.lower():
                produtos.append(Produto.produtos[produto])
                return produtos'''

