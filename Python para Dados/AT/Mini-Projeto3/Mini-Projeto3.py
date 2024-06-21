import pandas as pd
import sqlite3
from sqlalchemy import create_engine

PATH = 'Python para Dados\\AT\\Mini-Projeto3\\consolidado_jogos.xlsx'
DB_PATH = 'Python para Dados\\AT\\Mini-Projeto3\\banco_de_dados.sqlite'

# Função para ler o arquivo Excel
def read_excel_file(PATH):
    try:
        df = pd.read_excel(PATH)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

# Função para realizar operações com sets
def analyze_games(df):
    try:
        user_games = {}
        
        for index, row in df.iterrows():
            user = row['Usuário']
            games = row['Jogos'].split(',')
            games = [game.strip() for game in games]
            
            if user not in user_games:
                user_games[user] = set(games)
            else:
                user_games[user].update(games)
        
        all_games = set()
        unique_games = set()
        more_than_once_games = set()
        
        game_count = {}
        
        for games in user_games.values():
            all_games.update(games)
            for game in games:
                if game in game_count:
                    game_count[game] += 1
                    if game_count[game] == 2:
                        more_than_once_games.add(game)
                        unique_games.discard(game)
                else:
                    game_count[game] = 1
                    unique_games.add(game)
        
        return all_games, unique_games, more_than_once_games
    
    except Exception as e:
        print(f"Erro ao processar os jogos: {e}")
        return None, None, None

# Função para exportar dados para um banco de dados SQLite
def export_to_sqlite(data, DB_PATH):
    try:
        engine = create_engine(f'sqlite:///{DB_PATH}')
        conn = engine.connect()
        
        data.to_sql('games_analysis', conn, if_exists='replace', index=False)
        
        conn.close()
    except Exception as e:
        print(f"Erro ao exportar os dados para o banco de dados SQLite: {e}")


df = read_excel_file(PATH)
if df is not None:
    all_games, unique_games, more_than_once_games = analyze_games(df)
    
    if all_games is not None and unique_games is not None and more_than_once_games is not None:
        data = {
            'All Games': list(all_games),
            'Unique Games': list(unique_games),
            'More Than Once Games': list(more_than_once_games)
        }
        
        df_export = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
        
        export_to_sqlite(df_export, DB_PATH)
    else:
        print("Erro ao analisar os jogos.")
else:
    print("Erro ao ler o arquivo Excel.")

