# Você possui três arquivos Excel com dados de vendas dos primeiros três trimestres do ano. Cada arquivo contém dados de vendas com as colunas 'Data', 'Produto' e 'Quantidade'. Seu desafio é carregar esses arquivos em DataFrames separados, combiná-los em um único DataFrame e, em seguida, calcular o total de vendas por produto.

import pandas as pd 
# pip install openpyxl

df_trimestre1 = pd.read_excel('Python para Dados\\TP02\\ex7_Tab1.xlsx')
df_trimestre2 = pd.read_excel('Python para Dados\\TP02\\ex7_Tab2.xlsx')
df_trimestre3 = pd.read_excel('Python para Dados\\TP02\\ex7_Tab3.xlsx')

df_combined = pd.concat([df_trimestre1, df_trimestre2, df_trimestre3])
total_vendas = df_combined.groupby('Produto')['Quantidade'].sum().reset_index()

print("Todas as vendas:", total_vendas)
