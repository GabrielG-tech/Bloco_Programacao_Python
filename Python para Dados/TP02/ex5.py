# Imagine que você tenha dois arquivos Excel, cada um contendo dados de vendas de diferentes meses. Seu desafio é carregar ambos os arquivos em DataFrames, combinar os dados em um único DataFrame e calcular o total de vendas para cada produto. Finalmente, escreva o resultado em um novo arquivo Excel.

import pandas as pd
# pip install openpyxl

arquivo1 = "Python para Dados\\TP02\\ex5_Tab1.xlsx"
arquivo2 = "Python para Dados\\TP02\\ex5_Tab2.xlsx"

df1 = pd.read_excel(arquivo1)
df2 = pd.read_excel(arquivo2)

# Combinar os DataFrames
df_combinados = pd.concat([df1, df2]) # juntar DataFrames

# Calcular o total de vendas para cada produto
total_vendas = df_combinados.groupby('Produto')['Vendas'].sum().reset_index()

# Escrever o resultado em um novo arquivo Excel
resultado = "Python para Dados\\TP02\\ex5_resultado.xlsx"
total_vendas.to_excel(resultado, index=False)

print("Dados combinados e total de vendas calculado com sucesso! Resultado salvo em", resultado)
