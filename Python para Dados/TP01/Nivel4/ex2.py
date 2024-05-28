# Nivel 4 - Ex 2
# Leitura e Análise de Arquivos CSV: Desenvolva um programa que leia um arquivo CSV, processe os dados e execute cálculos estatísticos, como média, mediana e desvio padrão das colunas numéricas.

# pip install pandas
import pandas as pd

# ler o arquivo CSV e calcular as estatísticas
def calcular_estatisticas(arquivo_csv):
    dados = pd.read_csv(arquivo_csv)
    
    colunas_numericas = dados.select_dtypes(include='number')
    
    # Calcula a média, mediana e desvio padrão para cada coluna numérica
    estatisticas = {
        'media': colunas_numericas.mean(),
        'mediana': colunas_numericas.median(),
        'desvio_padrao': colunas_numericas.std()
    }
    return estatisticas

arquivo_csv = 'Python para Dados\\TP01\\Nivel4\\ex2.csv'
estatisticas = calcular_estatisticas(arquivo_csv)

# Exibe as estatísticas
print("Estatísticas das colunas numéricas:")
for estatistica, valores in estatisticas.items():
    print(f"\n{estatistica.capitalize()}:")
    print(valores)
