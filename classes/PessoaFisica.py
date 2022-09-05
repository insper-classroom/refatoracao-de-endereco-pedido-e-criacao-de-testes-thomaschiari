#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    pessoas = {}

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.pessoas[self.nome] = self

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        pass

    def get_endereco(self, apelido_endereco):
        pass

    def get_nome(self):
        return self.nome

    def busca_nome(nome):
        pessoas = []
        for pessoa in PessoaFisica.pessoas.keys():
            if pessoa == nome:
                pessoas.append(PessoaFisica.pessoas[pessoa])
                return pessoas

    def listar_enderecos(self):
        lista_enderecos = []
        for item, valor in self.__enderecos.items():
            lista_enderecos.append(item)
            lista_enderecos.append(repr(valor))
        return lista_enderecos
    
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.cpf}'
 