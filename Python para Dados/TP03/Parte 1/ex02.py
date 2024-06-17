# Crie um DataFrame com os seguintes dados do tipo: {'nome': ['Ana', 'Carlos'], 'idade': [25, 30], 'cidade': ['Rio de Janeiro', 'São Paulo']}. Conecte-se a um banco de dados SQLite (pessoas.db) e armazene o DataFrame em uma tabela chamada pessoas.

import pandas as pd
import sqlite3

<<<<<<< HEAD
PATH = 'Python para Dados\\TP03\\Parte 1\\'
DATABASE_PATH = PATH + 'ex02_pessoas.db'

=======
>>>>>>> 3b10b5f40c11c93c3ef70382dba06133ad908644
data = {
    'nome': ['Ana', 'Carlos'],
    'idade': [25, 30],
    'cidade': ['Rio de Janeiro', 'São Paulo']
}
df = pd.DataFrame(data)

<<<<<<< HEAD
# Conecta no banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect(DATABASE_PATH)

# Armazena o DataFrame na tabela pessoas
=======
# Conecta SQLite DB (ou criar se não existir)
conn = sqlite3.connect('ex02_pessoas.db')

# Armazena o DF na tabela "pessoas"
>>>>>>> 3b10b5f40c11c93c3ef70382dba06133ad908644
df.to_sql('pessoas', conn, if_exists='replace', index=False)
conn.close()

print("Dados armazenados na tabela 'pessoas' do banco de dados 'ex02_pessoas.db'")
