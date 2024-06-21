import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define o caminho para salvar o arquivo CSV
PATH = 'Python para Dados\\AT\\Mini-Projeto1\\Xbox360\\'

url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_360"
resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    tabela = soup.find('table', {'id': 'softwarelist'})

    # Extrai os cabeçalhos e as linhas da tabela
    colunas = [th.text.strip() for th in tabela.find('tr').find_all('th')[:-3] if not th.has_attr('colspan')]
    regioes = [th.text.strip() for th in tabela.find_all('tr')[1].find_all('th')]

    for linha in regioes:
        colunas.append(linha)

    linhas = []

    for linha in tabela.find_all('tr')[1:]:
        valores_linha = [td.text.strip() or '-' for td in linha.find_all('td')[:-3]]
        linhas.append(valores_linha)

    # Converte os dados em um DataFrame do pandas
    df = pd.DataFrame(linhas, columns=colunas)

    df.dropna(inplace=True) 
    df.drop_duplicates(inplace=True)  

    # Exporta o DataFrame para um arquivo CSV
    df.to_csv(f'{PATH}xbox360_jogos.csv', index=False)

else:
    print("Erro ao fazer a requisição:", resposta.status_code)
