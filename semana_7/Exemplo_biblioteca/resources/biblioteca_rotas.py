from flask_restful import Resource
from flask import request, jsonify
from model.biblioteca_modelos import AlunoModel, LivroModel





class ListaAlunos(Resource):

    def get(self):
        todos_alunos = AlunoModel.seach_all()

        lista = []
        for aluno in todos_alunos:
            lista.append(aluno.toDict())

        return {'alunos': lista }


class Aluno(Resource):

    def get(self, id):
        aluno = AlunoModel.find_by_id(id)

        if aluno:
            return aluno.toDict()

        return {'id': None}, 404


    def post(self, id):
        corpo = request.get_json( force=True )

        aluno = AlunoModel(id=id, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            aluno.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um aluno (DB)"}, 500

        return aluno.toDict(), 201

    def put(self, id):
        pass
    
    def delete(self, id):
        aluno = AlunoModel.find_by_id(id)

        if aluno:
            aluno.delete()
            return {'mensagem': 'Aluno deletado da base.'}

        return {'mensagem': 'Aluno não encontrado.'}, 404


class ListaLivros(Resource):
    
    def get(self):
        todos_livros = LivroModel.seach_all()

        lista = []
        for livro in todos_livros:
            lista.append(livro.toDict())

        return {'livros': lista }



class Livro(Resource):
    
    def get(self, id):
        livro = LivroModel.find_by_id(id)

        if livro:
            return livro.toDict()

        return {'id': None}, 404


    def post(self, id):
        corpo = request.get_json( force=True )

        livro = LivroModel(id = id, **corpo) #ProdutoModel(corpo['nome'], corpo['preco'])
        try:
            livro.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um livro (DB)"}, 500

        return livro.toDict(), 201

    def put(self, id):
        pass

            
    
    def delete(self, id):
        livro = LivroModel.find_by_id(id)

        if livro:
            livro.delete()
            return {'mensagem': 'Livro deletado.'}

        return {'mensagem': 'Livro não encontrado.'}, 404



class Emprestados(Resource):
    def get(self, id_aluno):
    
        aluno = AlunoModel.find_by_id(id_aluno)

        if aluno:
            lista_livros = []
            for livro in aluno.livros_em_posse:
                lista_livros.append({'nome':livro.nome, 'isbn':livro.isbn})

            return {f'livros em posse de {aluno.nome}': lista_livros}

        return {'id': None}, 404

        
# modelar emprestimo de livro
# devolução de livro
class EmprestimoLivro(Resource):

    def post(self):
        corpo = request.get_json( force=True )

        aluno = AlunoModel.find_by_id(corpo['id_aluno'])
        livro = LivroModel.find_by_id(corpo['id_livro'])

        if aluno and livro:
            aluno.livros_em_posse.append(livro)

        try:
            aluno.save()
        except:
            return {"menssagem":"Ocorreu um erro interno (DB)"}, 500

        return {"menssagem":f'Livro {livro.nome} emprestado para o aluno {aluno.nome}'}, 201


    def delete(self):
        corpo = request.get_json( force=True )

        aluno = AlunoModel.find_by_id(corpo['id_aluno'])
        livro = LivroModel.find_by_id(corpo['id_livro'])

        if aluno and livro:
            aluno.livros_emprestados.remove(livro)

        try:
            aluno.save()
        except:
            return {"menssagem":"Ocorreu um erro interno (DB)"}, 500

        return {"menssagem":f'Livro {livro.nome} foi devolvido pelo aluno {aluno.nome}'}, 201


