# Utilize um arquivo CSV de sua escolha (pode ser um conjunto de dados público sobre um tema de interesse) para realizar as seguintes tarefas com Pandas:
# A. Carregar os dados em um DataFrame.
# B. Realizar uma análise exploratória básica (número de linhas, colunas, tipos de dados).
# C. Limpar os dados se necessário (tratar valores ausentes, remover duplicatas).
# D. Criar novas colunas com dados derivados ou calculados.
# E. Salvar o DataFrame modificado em um novo arquivo CSV.

import pandas as pd

# Passo A: Carregar os dados em um DataFrame
df = pd.read_csv('Python para Dados\TP02\ex4.csv')

# Passo B: Realizar uma análise exploratória básica
print(f"Número de linhas: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")
print(df.dtypes) # tipagem das colunas
print(df.describe().round(2)) # resumo estatístico arredondado
print(df.isnull().sum()) # verificar dados ausentes

# Passo C: Limpar os dados se necessário
df = df.drop_duplicates() # remove valores duplicados (caso tenha)
df = df.dropna() # remove linhas sem valores)
print(df.isnull().sum())
print(f"Número de duplicatas: {df.duplicated().sum()}")

# Passo D: Criar novas colunas com dados derivados ou calculados
df['depreciacao_anual'] = (100000 - df['preco']) / (2024 - df['ano'])
df = df.round(2)
print(df.head())

# Passo E: Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('Python para Dados\\TP02\\ex4_novo.csv', index=False)
print("DataFrame modificado salvo em 'ex4_novo.csv'")
