import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define o caminho para salvar o arquivo CSV
PATH = 'Python para Dados\\AT\\Mini-Projeto1\\PlayStation5\\'

url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_5"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tabela = soup.find('table', {'id': 'softwarelist'})
    cabecalhos = []
    for th in tabela.find('tr').find_all('th'):
        if not th.has_attr('colspan'):
            cabecalhos.append(th.text.strip())
    cabecalhos = cabecalhos[:-2]

    # Extrai as regiões
    regioes = []
    for th in tabela.find_all('tr')[1].find_all('th'):
        regioes.append(th.text.strip())

    for region in regioes:
        cabecalhos.append(region)

    # Extrai as linhas da tabela
    linhas = []
    for linha in tabela.find_all('tr')[2:]:
        linha_valor = []
        for td in linha.find_all(['th', 'td']):
            linha_valor.append(td.text.strip() or '-')
        linhas.append(linha_valor[:-2])

    # Converte os dados em um DataFrame do pandas
    df = pd.DataFrame(linhas, columns=cabecalhos)

    # Faz a checagem e limpeza dos dados
    df.dropna(inplace=True)  # Remove linhas com valores nulos
    df.drop_duplicates(inplace=True)  # Remove linhas duplicadas

    # Exporta o DataFrame para um arquivo CSV
    df.to_csv(f'{PATH}ps5_jogos.csv', index=False)

else:
    print("Erro ao fazer a requisição:", response.status_code)
