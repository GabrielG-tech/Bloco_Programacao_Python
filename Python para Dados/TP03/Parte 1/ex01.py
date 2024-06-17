# Utilizando o SQLAlchemy, crie uma engine para conexão com um banco de dados sqlite de sua escolha, carregue ele para um DataFrame Pandas e exporte as informações para dois arquivos json diferentes, cada um com uma orientação.

# pip install sqlalchemy pandas
import sqlite3
from sqlalchemy import create_engine
import pandas as pd

PATH = 'Python para Dados\\TP03\\Parte 1\\'
DB_PATH = PATH + 'ex01_banco.db'
PATH_OUTPUT_RECORDS = PATH + 'ex01_data_records.json'
PATH_OUTPUT_SPLIT = PATH + 'ex01_data_split.json'

# def criarBanco():
#     # Criação do banco de dados e conexão
#     conn = sqlite3.connect(DATABASE_PATH)
#     cursor = conn.cursor()

#     # Criação da tabela 'data'
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS data (
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         idade INTEGER,
#         cidade TEXT
#     )
#     ''')

#     # dados de exemplo
#     cursor.executemany('''
#     INSERT INTO data (nome, idade, cidade)
#     VALUES (?, ?, ?)
#     ''', [
#         ('Ana', 23, 'São Paulo'),
#         ('Bruno', 34, 'Rio de Janeiro'),
#         ('Carlos', 45, 'Belo Horizonte'),
#         ('Daniela', 29, 'Curitiba'),
#         ('Eduardo', 39, 'Porto Alegre')
#     ])
#     conn.commit()
#     conn.close()
# criarBanco()

try:
    # Criação da engine de conexão com o banco de dados SQLite
    engine = create_engine(f'sqlite:///{DB_PATH}')

    # Carregamento dos dados da tabela 'data' para um DataFrame
    df = pd.read_sql_table('data', con=engine)

    # Exportação dos dados em orientação 'records'
    df.to_json(PATH_OUTPUT_RECORDS, orient='records', indent=4)

    # Exportação dos dados em orientação 'split'
    df.to_json(PATH_OUTPUT_SPLIT, orient='split', indent=4)

    print("Exportação concluída com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
