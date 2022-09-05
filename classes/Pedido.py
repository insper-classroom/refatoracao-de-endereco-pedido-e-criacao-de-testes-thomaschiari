#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re

class Pedido:

    def __init__(self, endereco_entrega='', endereco_faturamento='', pessoa: PessoaFisica = None, carrinho: Carrinho = None):
        self.endereco_entrega = endereco_entrega
        self.endereco_faturamento = endereco_faturamento
        self.status = 1
        self.pessoa = pessoa
        self.carrinho = carrinho

    def __str__(self):
        status_pedido = 'PAGO' if self.status == 2 else 'PENDENTE'
        return f'Nome: {self.pessoa.get_nome()} | Endereço de Entrega: {self.endereco_entrega} | Endereço de Faturamento: {self.endereco_faturamento} | Status do Pedido: {status_pedido} | Descrição do Pedido: {self.carrinho.get_itens()}'

    EM_ABERTO = 1
    PAGO = 2
    pass
    