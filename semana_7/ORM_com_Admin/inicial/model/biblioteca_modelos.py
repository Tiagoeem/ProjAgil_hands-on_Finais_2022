from __future__ import annotations
from model.sql_alchemy_para_db import db


class AlunoModel(db.Model):
    __tablename__ = 'aluno_model'

    id = db.Column( db.Integer, primary_key = True )
    nome = db.Column( db.String(100) )
    numero = db.Column( db.String(20) )

    def __init__(self, id, nome, numero):
        self.id = id
        self.nome = nome
        self.numero = numero  

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
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'numero':self.numero}