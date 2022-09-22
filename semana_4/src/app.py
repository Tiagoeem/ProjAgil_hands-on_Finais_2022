from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd


app = Flask(__name__)
app.list_of_dicts = []


def todos_registrados():
    return app.list_of_dicts[:1000]

def buscar_registrado_por_ean(ean):

    for reg in app.list_of_dicts:
        if ean == reg['ean']:
            return reg, True
    
    return None, False


# mais sobre a biblioteca pathlib: https://docs.python.org/3/library/pathlib.html
@app.before_first_request
def load_dados():
    FILE = Path(__file__).resolve()
    src_folder = FILE.parents[0]
    rel_arquivo = Path('recursos/itens.csv')
    # concatena os paths
    arquivo = src_folder / rel_arquivo
    
    data = pd.read_csv(arquivo.resolve(), encoding="utf-8")
    app.list_of_dicts = data[['ean', 'name']].dropna().to_dict(orient="records")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/registrado/", methods=['GET'])
def rota_buscar_todos_registrados():

    return jsonify(todos_registrados()), 200

@app.route("/registrado/<string:ean>", methods=['GET'])
def rota_buscar_registrado_por_ean(ean):

    registrado, sucesso = buscar_registrado_por_ean(ean)

    if sucesso:
        return registrado, 200
    else:
        return {'erro':'Produto não encontrado nos registros'}, 404

@app.route("/registrado/", methods=['POST'])
def rota_inserir_prod_no_registro():

    try:
        content = request.get_json()
    except:
        return {'erro':'Erro ao parsear o Json'}, 400

    resp, encontrado = buscar_registrado_por_ean( content['ean'] )

    if encontrado:
        return {'erro':'Produto já existe no registro'}, 400
    else:
        app.list_of_dicts.append( content )
        return content, 201
    
        


    



if __name__ == '__main__':
    app.run(debug=False)