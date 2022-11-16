from __future__ import annotations
from model.sql_alchemy_para_db import db


emprestimos = db.Table('tbl_emprestimos',
                    db.Column('aluno_id', db.Integer, db.ForeignKey('aluno_model.id')),
                    db.Column('livro_id', db.Integer, db.ForeignKey('livro_model.id'))
                    )

class AlunoModel(db.Model):
    _tablename__ = "aluno_model"

    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.String(80))
    numero = db.Column(db.String(20))
    livros_em_posse = db.relationship('LivroModel', secondary="tbl_emprestimos", backref='usuarios_com_emprestimos')

    def __init__(self, id, nome, numero):
        self.id = id
        self.nome = nome
        self.numero = numero
        #super(AlunoModel, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def seach_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'numero':self.numero}


class LivroModel(db.Model):
    _tablename__ = "livro_model"

    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.String(100))
    isbn = db.Column(db.String(20))

    def __init__(self, id, nome, isbn):
        self.id = id
        self.nome = nome
        self.isbn = isbn
        #super(LivroModel, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def seach_all(cls):
        return cls.query.all()        

    def toDict(self):
        lista_aluno = []
        for aluno in self.usuarios_com_emprestimos:
            lista_aluno.append(aluno.nome)

        return {'id': self.id, 'nome':self.nome, 'isbn':self.isbn, 'emprestimos':lista_aluno}
