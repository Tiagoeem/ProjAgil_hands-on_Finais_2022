#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

import copy

# Caso de uso em que criamos uma pessoa do zero, em seguida um produto, e  depois fechamos um pedido

# Cria uma pessoa 
pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
print(pessoa1)

# Cria  um endereço
end1 = Endereco('08320330', 430)
print(end1)

# Cria um outro endereço
end2 = Endereco('04546042', 300)
print(end2)

# Adiciona endereço à pessoa
pessoa1.adicionar_endereco('casa', end1)

print("Endereços da pessoa")
print(pessoa1.listar_enderecos())

pessoa1.adicionar_endereco('trabalho', end2)
print("Endereços da pessoa após inclusão")
print(pessoa1.listar_enderecos())

# Criando um produto
sabonete = Produto("0010342967", "Sabonete")

carrinho = Carrinho()
carrinho.adicionar_item(sabonete)

pedido = Pedido()
# Lembre-se de adicionar estes atributos ao endereço
pedido.endereco_entrega = copy.deepcopy(end1) 
pedido.endereco_faturamento = copy.deepcopy(end2)


pag = Pagamento(pedido)
pag.processa_pagamento()
if pag.pagamento_aprovado:
    pedido.status = Pedido.PAGO 

print("Pedido aguardando coleta")

## Pedido deve imprir todos os detalhes da compra - pessoa, endereço e produtos
print(pedido)




