from classes.Pedido import Pedido

class Pagamento:
    def __init__(self, pedido:Pedido):
        self.pedido = pedido 

    def processa_pagamento(self):
        pass 

    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        return True

    