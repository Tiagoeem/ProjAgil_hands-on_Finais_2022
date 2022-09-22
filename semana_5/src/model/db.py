import sqlite3
from pathlib import Path


# Operações basicas
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
rel_arquivo_db = Path('estoque.db')
db = Path(src_folder / rel_arquivo_db).resolve()


# Utilizado com a operação de SELECT
def select_query(sql, ean='0'):
    """
    Executa um SELECT query em uma conexão SQLite.\n
    Argumentos:
    sql -- SELECT Query SQL (por simplificação, não existe verificação)
    ean -- Valor a ser buscado, se None, retorna tudo
    Retorno:
    Registros da tabela na Base de exemplo e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        if ean=='0':
            # Executa a query
            cur.execute(sql)
            # Busca todos os registros
            record = cur.fetchall()
        else:
            # Forma segura que passar parâmetro para uma query SQL
            # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
            # Executa a query

            cur.execute(sql, (ean,))
            # Busca apenas um registro
            record = cur.fetchone()
        # Se não encontrou nenhum registro, sucesso é False. 
        # Atenção: Não encontrar registro não gera erro, por isso não irá passar pelo "except"
        if record==None:
            sucesso = False

    except:
        sucesso = False
        record = None
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    # Retorna a resposta da Base de Dados
    return record, sucesso


# Utilizado com a operação de INSERT
def insert_query(sql, data):
    """
    Executa um INSERT query.\n
    Argumentos:
    sql -- INSERT SQL Query
    data -- Dicionário com informações. Exemplo.: cliente: (ean, name)
    data = { 'ean': '121212121', 'name': 'Escova de cabelo' } (Exemplo)
    Retorno:
    ID gerado automaticamente pela base e indicação de sucesso (True/False)
    """
    # Estamos adicionando essa linha para que após a inserção do registro
    # seja retorna o id do cliente adicionado
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (data['ean'], data['name']))
        # Realiza o commit da operação
        conexao.commit()
    except:
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
        
    return sucesso


# Utilizado com a operação de UPDATE
def update_query(sql, data):
    """
    Executa um UPDATE query.\n
    Argumentos:
    sql -- UPDATE SQL Query
    id -- ID cliente que será atualizado
    data -- Dicionário com informações. Exemplo.: cliente: (ean, name)
    data = { 'ean': '121212121', 'name': 'Escova de cabelo' } (Exemplo)
    Retorno:
    Quantidade de registros alterados e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, ( data['name'], data['ean'] ))
        # Qtd de resgistros alterados
        update_rows = cur.rowcount # poderia ser utilizado para verificações
        conexao.commit()
    except:
        update_rows = 0
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    return update_rows, sucesso


# Utilizado com a operação de DELETE
def delete_query(sql, ean):
    """
    Executa um DELETE query.\n
    Argumentos:
    sql -- DELETE SQL Query
    ean -- ean que será deletado
    Retorno:
    Quantidade de registros alterados e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (ean,))
        # Qtd de registros deletados
        deleted_rows = cur.rowcount
        # Realiza o commit da operação
        conexao.commit()
    except:
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    return deleted_rows, sucesso

