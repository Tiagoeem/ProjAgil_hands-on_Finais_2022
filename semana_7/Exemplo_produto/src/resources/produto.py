from flask_restful import Resource
from flask import request
from model.produto import LojaModel, ProdutoModel


class ListaProdutos(Resource):

    def get(self):
        todos_prod = ProdutoModel.seach_all()

        lista = []
        for prod in todos_prod:
            lista.append(prod.toDict())

        return {'produtos': lista }


class Produto(Resource):

    def get(self, id):
        prod = ProdutoModel.find_by_id(id)

        if prod:
            return prod.toDict()

        return {'id': None}, 404


    def post(self, id):
        corpo = request.get_json( force=True )

        produto = ProdutoModel(**corpo) #ProdutoModel(corpo['nome'], corpo['preco'])
        try:
            produto.save()
        except:
            return {"message":"Ocorreu um erro interno ao tentar inserir um item (DB)"}, 500

        return produto.toDict(), 201

    def put(self, id):
        pass

            
    
    def delete(self, id):
        prod = ProdutoModel.find_by_id(id)

        if prod:
            prod.delete()
            return {'message': 'Item deletado.'}

        return {'message': 'Item não encontrado.'}, 404


class ListaLojas(Resource):
    
    def get(self):
        todoas_lojas = LojaModel.seach_all()

        lista = []
        for loja in todoas_lojas:
            lista.append(loja.toDict())

        return {'lojas': lista }



class Loja(Resource):
    
    def get(self, id):
        loja = LojaModel.find_by_id(id)

        if loja:
            return loja.toDict()

        return {'id': None}, 404


    def post(self, id):
        corpo = request.get_json( force=True )

        loja = LojaModel(**corpo) #ProdutoModel(corpo['nome'], corpo['preco'])
        try:
            loja.save()
        except:
            return {"message":"Ocorreu um erro interno ao tentar inserir um item (DB)"}, 500

        return loja.toDict(), 201

    def put(self, id):
        pass

            
    
    def delete(self, id):
        loja = LojaModel.find_by_id(id)

        if loja:
            loja.delete()
            return {'message': 'Item deletado.'}

        return {'message': 'Item não encontrado.'}, 404