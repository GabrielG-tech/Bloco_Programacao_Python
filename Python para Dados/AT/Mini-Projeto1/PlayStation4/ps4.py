import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define o caminho para salvar o arquivo CSV
PATH = 'Python para Dados\\AT\\Mini-Projeto1\\PlayStation4\\'

def requisicao_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print("Erro ao fazer a requisição:", response.status_code)
        return None

def extrair_cabecalhos(tabela):
    return [th.text.strip() for th in tabela.find_all('tr')[0].find_all('th')][:-1]

def extrair_linhas(tabela):
    linhas = []
    for linha in tabela.find_all('tr')[1:]:
        linha_valor = []
        for td in linha.find_all(['td', 'th'])[:-1]:
            text = td.text.strip()
            if not text:
                text = 'Não definido'
            linha_valor.append(text)
        linhas.append(linha_valor)
    return linhas

def criar_dataframe(linhas, cabecalhos):
    df = pd.DataFrame(linhas, columns=cabecalhos)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def salvar_csv(df, caminho, nome_arquivo):
    df.to_csv(f'{caminho}{nome_arquivo}', index=False)

url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_4"
soup = requisicao_url(url)
if soup:
    tabela = soup.find('table', {'class': 'wikitable sortable'})
    cabecalhos = extrair_cabecalhos(tabela)
    linhas = extrair_linhas(tabela)
    df = criar_dataframe(linhas, cabecalhos)
    salvar_csv(df, PATH, 'ps4_jogos.csv')
