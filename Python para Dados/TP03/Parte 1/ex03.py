# Use o arquivo csv “dadoSujoTP3.csv” do repositório compartilhado com a turma, carregue-o para um DataFrame e proceda o tratamento de dados inicial, visualizando o dados, realizando uma análise exploratória básica para identificar dados vazios, inconsistentes ou com tipo errado. Realize a limpeza dos dados, adicione duas colunas geradas a partir dos dados existentes e exporte o DataFrame para um arquivo excel.

import pandas as pd

PATH = 'Python para Dados\\TP03\\Parte 1\\dadoSujoTP3.csv'
df = pd.read_csv(PATH)

# análise exploratória básica:
print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nInformações sobre o DataFrame:")
print(df.info())

print("\nValores nulos por coluna:")
print(df.isnull().sum())

# padronização das datas
df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce').dt.strftime('%Y-%m-%d')
df['data_inscricao'] = pd.to_datetime(df['data_inscricao'], errors='coerce').dt.strftime('%Y-%m-%d')

# correção de emails inválidos
df['email'] = df['email'].str.replace('example..com', 'example.com')
df['email'] = df['email'].apply(lambda x: x if pd.notnull(x) and '@' in x else 'email.desconhecido@example.com')

# remoção de duplicatas
df = df.drop_duplicates()

# substitui todos os valores NaN (valores ausentes) na coluna idade pela média calculada dessa coluna.
df['idade'] = df['idade'].fillna(df['idade'].mean())

# transforma idade em int
df['idade'] = df['idade'].astype(int)

# correção de preços e total de vendas (substitui os valores 100.000,00 em total_venda por 10.000,00.)
df.loc[df['total_venda'] == 100000.00, 'total_venda'] = 10000.00

# substitui todos os valores NaN (valores ausentes) na coluna preco_unitario por 0.
df['preco_unitario'] = df['preco_unitario'].fillna(0)

# remover telefone inválido
df['telefone'] = df['telefone'].fillna('N/A')

# salvar o CSV limpo:
OUTPUT_PATH_EXCEL = 'Python para Dados\\TP03\\Parte 1\\dadoLimpoTP3.xlsx'
df.to_excel(OUTPUT_PATH_EXCEL, index=False)

print(f"\nDataFrame limpo exportado para {OUTPUT_PATH_EXCEL}")
