# Utilizar um arquivo CSV de sua escolha (pode ser um conjunto de dados público sobre um tema de interesse) para realizar as seguintes tarefas com Pandas:

# Carregar os dados em um DataFrame.
# Realizar uma análise exploratória básica (número de linhas, colunas, tipos de dados).
# Limpar os dados se necessário (tratar valores ausentes, remover duplicatas).
# Criar novas colunas com dados derivados ou calculados.
# Salvar o DataFrame modificado em um novo arquivo CSV.

# pip install pandas
import pandas as pd

# Carregar os dados em um DataFrame
PATH = 'C:\\Users\\gabriel.gsouza\\Documents\\Bloco_Programacao_Python\\dataSujo.csv'
df = pd.read_csv(PATH)

df.head() # 5 primeiros valores
df.tail(10) # 10 ultimos valores
# df.info()

# Realizar uma análise exploratória básica
print("Número de linhas e colunas:", df.shape)
print("\nTipos de dados:\n", df.dtypes)
print("\nResumo estatístico:\n", df.describe())

# Tratar valores ausentes e remover duplicatas
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Criar novas colunas com dados derivados ou calculados
df['TotalCalories'] = df['Calories'].cumsum()
df['Potencia'] = df['Calories'] / df['Duration']

# Salvar o DataFrame modificado em um novo arquivo CSV com no máximo 2 casas decimais
df.to_csv('dataLimpo.csv', index=False, float_format='%.2f')

print("\nDataFrame modificado salvo em 'dataLimpo.csv'")
