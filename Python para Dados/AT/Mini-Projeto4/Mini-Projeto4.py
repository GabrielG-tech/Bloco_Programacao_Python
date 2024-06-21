import requests
import pandas as pd
import time
import sqlite3
from sqlalchemy import create_engine

PATH_GAMES = 'Python para Dados\\AT\\Mini-Projeto4\\lista_de_jogos.txt' 
DB_PATH = 'Python para Dados\\AT\\Mini-Projeto4\\jogos_mercado_livre.db'

# Função para ler a lista de jogos de um arquivo
def ler_lista_de_jogos(PATH_GAMES):
    try:
        with open(PATH_GAMES, 'r') as file:
            jogos = file.read().splitlines()
        return jogos
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

# Função para consultar a API do Mercado Livre
def consultar_api_mercado_livre(jogo):
    url = f"https://api.mercadolibre.com/sites/MLB/search?category=MLB186456&q={jogo}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API para o jogo {jogo}: {e}")
        return None

# Função para extrair informações relevantes da resposta da API
def extrair_informacoes(dados):
    if dados and 'results' in dados:
        informacoes = []
        for item in dados['results']:
            nome = item.get('title')
            preco = item.get('price')
            permalink = item.get('permalink')
            informacoes.append((nome, preco, permalink))
        return informacoes
    else:
        return []

# Função para salvar os dados em um banco de dados SQL
def salvar_em_banco_de_dados(dados, DB_PATH):
    try:
        engine = create_engine(f'sqlite:///{DB_PATH}')
        df = pd.DataFrame(dados, columns=['Nome', 'Preço', 'Permalink'])
        df.to_sql('jogos', con=engine, if_exists='replace', index=False)
        print(f"Dados salvos com sucesso no banco de dados {DB_PATH}")
    except Exception as e:
        print(f"Erro ao salvar os dados no banco de dados: {e}")

jogos = ler_lista_de_jogos(PATH_GAMES)

todos_os_dados = []
for jogo in jogos:
    dados = consultar_api_mercado_livre(jogo)
    informacoes = extrair_informacoes(dados)
    todos_os_dados.extend(informacoes)
    time.sleep(1)  # Atraso entre as consultas para respeitar os limites de taxa da API

if todos_os_dados:
    salvar_em_banco_de_dados(todos_os_dados, DB_PATH)
else:
    print("Nenhum dado foi extraído.")
