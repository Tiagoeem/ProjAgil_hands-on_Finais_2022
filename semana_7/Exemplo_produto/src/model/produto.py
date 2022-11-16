from model.db import db


class Association(db.Model):
    __tablename__ = "association"
    loja_id = db.Column(db.ForeignKey("tbl_loja.id"), primary_key=True)
    produto_id = db.Column(db.ForeignKey("tbl_produto.id"), primary_key=True)
    qtd = db.Column(db.Integer)

    lojas = db.relationship("ProdutoModel", backref="lojas")
    produtos = db.relationship("LojaModel", backref="produtos")


class ProdutoModel(db.Model):
    _tablename__ = "tbl_produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    preco = db.Column(db.Float(precision=2))
    lojas = db.relationship("Association", back_populates="lojas")

    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
    def __init__(self, nome, preco, **kwargs):
        self.nome = nome
        self.preco = preco
        super(ProdutoModel, self).__init__(**kwargs)

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'preco':self.preco}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def seach_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class LojaModel(db.Model):
    __tablename__ = "tbl_loja"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    produtos = db.relationship("Association", back_populates="produtos")
    #preco = db.Column(db.Float(precision=2))

    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
    def __init__(self, nome, **kwargs):
        self.nome = nome
        super(ProdutoModel, self).__init__(**kwargs)

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'preco':self.preco}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def seach_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()  