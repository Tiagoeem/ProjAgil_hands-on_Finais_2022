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
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd):
        
        id = item.get_id()
        
        # Implemente a adição do item no dicionário
        

    def remover_item(self, item:Produto):
        pass
        # Implemente este método
