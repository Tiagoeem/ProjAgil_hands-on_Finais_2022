import sqlite3
import pandas as pd
from pathlib import Path

# Armazenando referância para raiz do projeto
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]


def criar_db(caminho_arq_db):

    # Conecta com a base, se não existe cria
    con = sqlite3.connect(caminho_arq_db.resolve())

    # Cria o cursor de conexão com a base
    cur = con.cursor()

    tabela_nome = 'tbl_registrados'

    # Se a tabela já existe é deletada
    cur.execute(f'DROP TABLE IF EXISTS {tabela_nome}')

    # Cria a tabela zerada
    comando_sql =f'''CREATE TABLE {tabela_nome} (
        "uid"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "ean"	TEXT,
        "name"	TEXT
    )'''
    # executa o comando sql armazenado na variavel sql
    cur.execute(comando_sql)

    # commita as alterações
    con.commit()

    # fecha a conexão com a base
    con.close()


def load_tabela_registrados(caminho_arq_db, caminho_csv):
    # realizando a carga de varios valores na tabela tbl_registrados

    list_of_dicts = []

    data = pd.read_csv(caminho_csv.resolve(), encoding="utf-8")
    list_of_dicts = list(data[['ean', 'name']].dropna().head(2000).itertuples(index=False, name=None))


    con = sqlite3.connect(caminho_arq_db.resolve())

    # https://docs.python.org/2/library/sqlite3.html#sqlite3-controlling-transactions
    # Fill the table
    comando_sql = "INSERT INTO tbl_registrados(ean, name) VALUES (?, ?)"
    con.executemany(comando_sql, list_of_dicts)

    # commita as alterações
    con.commit()

    # fecha a conexão com a base
    con.close()


# caminho para a base
rel_arquivo_db = Path('estoque.db')
caminho_arq_db = src_folder / rel_arquivo_db

# caminho para o arquivo csv
rel_arquivo_itens = Path('../recursos/itens.csv')
arquivo_csv = src_folder / rel_arquivo_itens

# Cria a base com uma tabela
criar_db(caminho_arq_db)

# carrega os dados do csv para a tabela
load_tabela_registrados(caminho_arq_db, arquivo_csv)