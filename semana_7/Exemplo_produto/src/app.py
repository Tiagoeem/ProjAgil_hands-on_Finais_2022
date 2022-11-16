from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path

from model.db import db
from resources.produto import Produto, ListaProdutos, Loja, ListaLojas


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/loja.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
#https://docs.sqlalchemy.org/en/14/core/engines.html
## Windows
#engine = create_engine("sqlite:///C:\\path\\to\\foo.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////model/loja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>{p.nome}"

api.add_resource(Produto, '/produto/<int:id>')
api.add_resource(ListaProdutos, '/produto')
api.add_resource(Loja, '/loja/<int:id>')
api.add_resource(ListaLojas, '/loja')


if __name__ == '__main__':
    db.init_app(app)
    #db.create_all()
    app.run(debug=True)