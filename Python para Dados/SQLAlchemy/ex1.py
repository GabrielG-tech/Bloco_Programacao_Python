import pandas as pd
from sqlalchemy import create_engine

# Criando uma conexão com o banco de dados
engine = create_engine(f'sqlite:///Python para Dados/SQLAlchemy/banco_de_dados.db', echo=True)

# Dados que você deseja inserir na tabelaNova
dados = {
    'coluna1': [1, 2, 3],
    'coluna2': ['a', 'b', 'c']
}

# Criando um DataFrame com os dados
df_novos_dados = pd.DataFrame(dados)

# Inserindo os dados na tabelaNova
df_novos_dados.to_sql('tabelaNova', engine, if_exists='append', index=False)

# Lendo os dados da tabelaNova para verificar se os dados foram inseridos com sucesso
df_sql = pd.read_sql_query("SELECT * FROM tabelaNova", engine)
print(df_sql)
