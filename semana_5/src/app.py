from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd
from model.db import delete_query, select_query, insert_query, update_query
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class ItemRegistrado(Resource):


    def __init__(self) -> None:
        super().__init__(nome)

    # lê um item registrado
    def get(self, ean):
        cmd_sql = 'select * from tbl_registrados WHERE ean = ?'
        registrado, sucesso = select_query(cmd_sql, ean)

        resp = {'uid':registrado[0], 'ean':registrado[1], 'name':registrado[2]}

        if sucesso:
            return resp, 200
        else:
            return {'erro':'Produto não encontrado nos registros'}, 404

    # adiciona um item
    def post(self, ean):
        try:
            content = request.get_json()
        except:
            return {'erro':'Erro ao parsear o Json'}, 400

        cmd_sql = 'select * from tbl_registrados WHERE ean = ?'
        registrado, encontrado = select_query(cmd_sql, ean)

        if not(encontrado):
            cmd_sql = 'insert into tbl_registrados(ean, name) values (?, ?)'
            dado = {'ean': ean, 'name':content['name']}
            sucesso = insert_query(cmd_sql, dado)
            if sucesso:
                return {'mensagem':f'Produto {content["name"]} registrado com sucesso'}, 201
            else:
                return {'erro':'Erro interno'}, 500    
        else:
            return {'erro':'Produto já existe no registro'}, 400


    # altera um item registrado
    def put(self, ean):
        try:
            content = request.get_json()
        except:
            return {'erro':'Erro ao parsear o Json'}, 400

        cmd_sql = 'select * from tbl_registrados WHERE ean = ?'
        registrado, encontrado = select_query(cmd_sql, ean)

        if encontrado:
            cmd_sql = 'update tbl_registrados set name = ? WHERE ean = ?'
            dado = {'ean': ean, 'name':content['name']}
            linhas_afetadas, sucesso = update_query(cmd_sql, dado)
            if sucesso:
                return {'mensagem':f'{linhas_afetadas} foram atualizadas com sucesso'}, 200
            else:
                return {'erro':'Erro interno'}, 500    
        else:
            return {'erro':'Produto já existe no registro'}, 400

    # deleta um item do registro
    def delete(self, ean):
        
        return '', 204


class ListaItemRegistrados(Resource):

    def get(self):
        cmd_sql = 'select * from tbl_registrados'
        resultado = select_query(cmd_sql)
        return resultado, 200


##
## Setup e ligação entre as rotas e os registros
##
api.add_resource(ItemRegistrado, '/registrado/<ean>' )
api.add_resource(ListaItemRegistrados, '/registrado' )


if __name__ == '__main__':
    app.run(debug=True)