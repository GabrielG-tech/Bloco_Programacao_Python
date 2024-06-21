import requests
import pandas as pd
import time
import sqlite3
from sqlalchemy import create_engine
# import sqlalchemy as db

PATH = 'Python para Dados\\AT\\Mini-Projeto3\\banco_de_dados.sqlite' 
DB_PATH = 'Python para Dados\\AT\\Mini-Projeto4\\jogos_mercado_livre.db'

def conectar_banco_de_dados(db_path, path):
    engine = create_engine(f'sqlite:///{db_path}')
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    return engine, conn, cursor

def ler_jogos_separados(cursor):
    cursor.execute('SELECT Jogo FROM jogos_separados')
    jogos_separados = [row[0] for row in cursor.fetchall()]
    return jogos_separados

def API_consulta(jogo):
    """
    Consulta a API do Mercado Livre para obter informações do jogo.
    """
    url = f'https://api.mercadolibre.com/sites/MLB/search?category=MLB186456&q={jogo.replace(" ", "%20")}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['results']

def processar_resultados(resultados, df):
    """
    Processa os resultados da consulta à API e adiciona ao DataFrame.
    """
    for result in resultados:
        nome = result['title']
        preco = result['price']
        permalink = result['permalink']
        df.loc[len(df)] = [nome, preco, permalink]

def exportar_para_banco_de_dados(df, engine):
    """
    Exporta o DataFrame para o banco de dados SQLite.
    """
    df.to_sql('jogos_mercado_livre', engine, if_exists='replace', index=False)

engine, conn, cursor = conectar_banco_de_dados(DB_PATH, PATH)
jogos_separados = ler_jogos_separados(cursor)

# Criar um DataFrame para armazenar os dados
df = pd.DataFrame(columns=['nome', 'preco', 'permalink'])

for jogo in jogos_separados:
    try:
        resultados = API_consulta(jogo)
        processar_resultados(resultados, df)
        time.sleep(1) # evitar problema com API
    except requests.exceptions.RequestException as e:
        print(f'Erro ao consultar a API: {e}')
    except Exception as e:
        print(f'Erro ao processar a resposta: {e}')

# Exportar o DataFrame para o banco de dados
exportar_para_banco_de_dados(df, engine)

# Fechar a conexão com o banco de dados
conn.close()
