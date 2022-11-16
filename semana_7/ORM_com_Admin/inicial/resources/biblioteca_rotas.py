from flask_restful import Resource
from flask import request

from model.biblioteca_modelos import AlunoModel

class ListaAlunos(Resource):

    def get(self):

        todos_alunos = AlunoModel.search_all()

        lista = []
        for aluno in todos_alunos:
            lista.append(aluno.toDict())

        return {'alunos': lista}, 200


class Aluno(Resource):

    def get(self, id):

        aluno = AlunoModel.find_by_id(id)
        
        if aluno:
            return aluno.toDict(), 200

        return {'mensagem': 'Aluno não encontrado'}, 404


    def post(self, id):

        aluno = AlunoModel.find_by_id(id)
        
        if aluno:
            return {"mensagem":"Id de aluno já existe"}, 400
        else:

            corpo = request.get_json( force=True )

            print(corpo)
            #aluno = AlunoModel(id=id, nome=corpo['nome'], numero=corpo['numero'])
            aluno = AlunoModel(id=id, **corpo)

            try:
                aluno.save()
            except:
                return {"mensagem":"Ocorreu um erro interno ao tentar inserir um aluno (DB)"}, 500

            return aluno.toDict(), 201
