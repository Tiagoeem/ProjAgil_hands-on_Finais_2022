#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto

p = Produto(88)
print(p)
print(p.to_dict())

p2 = Produto(87, 'Sabao')
print(p2)

# p.__id = 10
p.set_id(10)
print(p.to_dict())

p.nome = 'Tabio'
print(p.to_dict())

end = Endereco('08320330', 400)
print(end)


#pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
#print(pessoa1)


#end1 = Endereco('08320330', 430)
#print(end1)

#end2 = Endereco('04546042', 300)
#print(end2)

#pessoa1.adicionar_endereco('casa', end1)

#print(pessoa1.listar_enderecos())

#pessoa1.adicionar_endereco('trabalho', end2)

#print(pessoa1.listar_enderecos())