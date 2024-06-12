# Dado um DataFrame contendo informações sobre filmes (titulo, gênero, ano de lançamento), converta-o para o formato JSON. Em seguida, carregue esse JSON de volta para um DataFrame e adicione uma nova coluna com a duração dos filmes. Salve o DataFrame final como um novo arquivo JSON.

import pandas as pd
import json

data = {
    'titulo': ['Filme 1', 'Filme 2', 'Filme 3'],
    'genero': ['Ação', 'Comédia', 'Drama'],
    'ano_lancamento': [2020, 2019, 2018]
}
df = pd.DataFrame(data)

# Converte o DataFrame para JSON:
df_json = df.to_json(orient='records', indent=4) # lista de dicionários

with open('Python para Dados\\TP02\\ex6.json', 'w', encoding='utf-8') as f:
    f.write(df_json)

with open('Python para Dados\\TP02\\ex6.json', 'r', encoding='utf-8') as f:
    df_loaded = pd.read_json(f)

df_loaded['duracao'] = [120, 90, 110]

df_loaded.to_json('Python para Dados\\TP02\\ex6_filmes.json', orient='records', indent=4)
