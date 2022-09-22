#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Produto:

    def __init__(self, id_produto, nome=''):
        self.__id = id_produto
        self.__nome = nome

    def set_id(self, id_novo):
        self.__id = id_novo

    def get_id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome[0] != 'T':
            self.__nome = novo_nome

    @nome.getter
    def nome(self):
        return self.__nome

    def to_dict(self):
        return {'id': self.__id, 'nome': self.nome}
