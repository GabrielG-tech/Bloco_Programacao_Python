from sqlalchemy import create_engine
import pandas as pd

# Criando uma conexão ao banco (exemplo SQLite)
engine = create_engine('sqlite:///banco_de_dados.db')

# Carregando dados via consulta SQL
#df_sql = pd.read_sql_query("SELECT * FROM sua_tabela", engine)