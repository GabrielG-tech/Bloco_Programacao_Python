# Importações necessárias
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
import json

# Configuração do caminho do banco de dados e SQLAlchemy
PATH = 'Python_para_Dados/AT/ProjetoIntegrador/'
engine = create_engine(f'sqlite:///{PATH}/banco_jogos.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Função para importar dados de CSV e inserir no banco de dados
def importar_dados(csv_path, table):
    data = pd.read_csv(csv_path)
    try:
        data.to_sql(table, con=engine, if_exists='append', index=False)
        print(f'Dados importados para a tabela {table} com sucesso.')
    except Exception as e:
        print(f'Erro ao importar dados para a tabela {table}: {e}')

# Exemplo de uso da função de importação
# importar_dados('path_to_csv/consoles.csv', 'consoles')

# Função para exportar dados do banco de dados para CSV
def exportar_dados(table, export_path):
    try:
        df = pd.read_sql_table(table, con=engine)
        df.to_csv(export_path, index=False)
        print(f'Dados exportados da tabela {table} para {export_path} com sucesso.')
    except Exception as e:
        print(f'Erro ao exportar dados da tabela {table}: {e}')

# Exemplo de uso da função de exportação
# exportar_dados('consoles', 'path_to_export/consoles_export.csv')
