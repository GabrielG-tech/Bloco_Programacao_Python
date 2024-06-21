from sqlalchemy import create_engine
import requests
import pandas as pd
import time
import sqlite3

PATH = 'Python para Dados\\AT\\Mini-Projeto3\\banco_de_dados.sqlite' 
DB_PATH = 'Python para Dados\\AT\\Mini-Projeto4\\mercado_livre.db'

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
    try:
        url = f'https://api.mercadolibre.com/sites/MLB/search?category=MLB186456&q={jogo.replace(" ", "%20")}'
        response = requests.get(url)
        response.raise_for_status() # Lança uma exceção se a resposta da API tiver um código de erro
        return response.json()['results']
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
                                                            
def processar_dados(dados, df):
    for dado in dados:
        nome = dado['title']
        preco = dado['price']
        permalink = dado['permalink']
        df.loc[len(df)] = [nome, preco, permalink]
        print(nome, "processado.")

def exportar_db(df, engine):
    try:
        df.to_sql('jogos_mercado_livre', engine, if_exists='replace', index=False)
        print("Dados exportados com sucesso!")
    except Exception as e:
        print(f'Erro ao exportar para o banco de dados: {e}')

engine, conn, cursor = conectar_banco_de_dados(DB_PATH, PATH)
jogos_separados = ler_jogos_separados(cursor)

# Cria um DF para por os dados 
df = pd.DataFrame(columns=['nome', 'preco', 'permalink'])

for jogo in jogos_separados:
    try:
        dados = API_consulta(jogo)
        processar_dados(dados, df)
        time.sleep(1.5) # evitar problema com API
    except requests.exceptions.RequestException as e:
        print(f'Erro ao consultar a API: {e}')
    except Exception as e:
        print(f'Erro ao processar a resposta: {e}')

exportar_db(df, engine)
conn.close()
