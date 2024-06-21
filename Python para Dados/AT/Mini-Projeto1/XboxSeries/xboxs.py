import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define o caminho para salvar o arquivo CSV
PATH = 'Python para Dados\\AT\\Mini-Projeto1\\XboxSeries\\'

url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_Series_X_e_Series_S"
resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    tabela = soup.find('table', {'id': 'softwarelist'})

    # Extrai os cabeçalhos e as linhas da tabela
    cabecalhos = [th.text.strip() for th in tabela.find('tr').find_all('th') if not th.has_attr('colspan')][:-2]
    regioes = [th.text.strip() for th in tabela.find_all('tr')[1].find_all('th')]

    for linha in regioes:
        cabecalhos.append(linha)

    linhas = []

    for linha in tabela.find_all('tr')[1:]:
        valores_linha = [td.text.strip() for td in linha.find_all(['th', 'td'])[:-2]]
        linhas.append(valores_linha)

    # Converte os dados em um DataFrame do pandas
    df = pd.DataFrame(linhas, columns=cabecalhos)

    df.dropna(inplace=True)  
    df.drop_duplicates(inplace=True)  

    # Exporta o DataFrame para um arquivo CSV
    df.to_csv(f'{PATH}xbox_series_jogos.csv', index=False)

else:
    print("Erro ao fazer a requisição:", resposta.status_code)
