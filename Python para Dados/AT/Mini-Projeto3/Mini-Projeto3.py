import pandas as pd
from sqlalchemy import create_engine
import collections

EXCEL_PATH = 'Python para Dados\\AT\\Mini-Projeto2\\usuarios-consolidados.xlsx'
DB_PATH = 'Python para Dados\\AT\\Mini-Projeto3\\banco_de_dados.sqlite'

# Função para ler o arquivo Excel
def ler_arquivo_excel(caminho):
    try:
        df = pd.read_excel(caminho)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

def jogos_separados(df):
    jogos = set()
    for row in df['jogos_preferidos']:
        jogos.update(row.split('|'))
    return jogos # lista com todos os jogos separados

def jogos_populares(df):
    jogos = set()
    for row in df['jogos_preferidos']:
        jogos.update(row.split('|'))
    
    contador = collections.Counter()
    for row in df['jogos_preferidos']:
        contador.update(row.split('|'))
    
    jogos_populares = contador.most_common(5) # Retorna os 5 jogos mais comuns
    return jogos_populares

def jogos_especificos(df):
    jogos = set()
    for row in df['jogos_preferidos']:
        jogos.update(row.split('|'))
    
    contador = collections.Counter()
    for row in df['jogos_preferidos']:
        contador.update(row.split('|'))

    jogos_especificos = [jogo for jogo, contagem in contador.items() if contagem == 1]

    return jogos_especificos # Jogos que foram citados uma única vez

# Função para exportar dados para um banco de dados SQLite
def exportar_sqlite(db_path, jogos_separados, jogos_populares, jogos_especifico):
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        conn = engine.connect()
        
        pd.DataFrame(list(jogos_separados), columns=['Jogo']).to_sql('jogos_separados', engine, if_exists='replace', index=False)

        pd.DataFrame(list(jogos_populares), columns=['Jogo', 'Quantidade']).to_sql('jogos_populares', engine, if_exists='replace', index=False)

        pd.DataFrame(list(jogos_especifico), columns=['Jogo']).to_sql('jogos_especifico', engine, if_exists='replace', index=False)

        print(f"Dados exportados com sucesso no dados!")
        
    except Exception as e:
        print(f"Erro ao exportar os dados para o banco de dados SQLite: {e}")
    conn.close()

df = ler_arquivo_excel(EXCEL_PATH)

separados = jogos_separados(df)
populares = jogos_populares(df)
especifico = jogos_especificos(df)

exportar_sqlite(DB_PATH, separados, populares, especifico)
