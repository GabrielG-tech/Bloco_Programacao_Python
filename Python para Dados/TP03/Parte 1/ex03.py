# Use o arquivo csv “dadoSujoTP3.csv” do repositório compartilhado com a turma, carregue-o para um DataFrame e proceda o tratamento de dados inicial, visualizando o dados, realizando uma análise exploratória básica para identificar dados vazios, inconsistentes ou com tipo errado. Realize a limpeza dos dados, adicione duas colunas geradas a partir dos dados existentes e exporte o DataFrame para um arquivo excel.

import pandas as pd

PATH = 'Python para Dados\\TP03\\Parte 1\\dadoSujoTP3.csv'
df = pd.read_csv(PATH)

# Análise exploratória básica
print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nInformações sobre o DataFrame:")
print(df.info())

print("\nValores nulos por coluna:")
print(df.isnull().sum())

# fazer limpagem dos dados

OUTPUT_PATH_EXCEL = 'Python para Dados\\TP03\\Parte 1\\dadoLimpoTP3.xlsx'
df.to_excel(OUTPUT_PATH_EXCEL, index=False)

print(f"\nDataFrame limpo exportado para {OUTPUT_PATH_EXCEL}")
