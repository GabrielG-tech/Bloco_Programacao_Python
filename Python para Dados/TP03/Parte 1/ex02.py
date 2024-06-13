# Crie um DataFrame com os seguintes dados do tipo: {'nome': ['Ana', 'Carlos'], 'idade': [25, 30], 'cidade': ['Rio de Janeiro', 'São Paulo']}. Conecte-se a um banco de dados SQLite (pessoas.db) e armazene o DataFrame em uma tabela chamada pessoas.

import pandas as pd
import sqlite3

# Criar o DataFrame com os dados fornecidos
data = {
    'nome': ['Ana', 'Carlos'],
    'idade': [25, 30],
    'cidade': ['Rio de Janeiro', 'São Paulo']
}
df = pd.DataFrame(data)

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('ex02_pessoas.db')

# Armazenar o DataFrame na tabela pessoas
df.to_sql('pessoas', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print("Dados armazenados na tabela 'pessoas' do banco de dados 'ex02_pessoas.db'")
