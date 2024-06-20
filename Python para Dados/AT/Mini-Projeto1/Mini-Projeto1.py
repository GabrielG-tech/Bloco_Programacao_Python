import requests
from bs4 import BeautifulSoup
import pandas as pd

# Caminho para os arquivos exportados
PATH = 'Python para Dados\\AT\\Mini-Projeto1\\Arquivos_Exportados\\'

# Lista de URLs das páginas da Wikipédia
urls = {
    'PS5': 'https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_5',
    'PS4': 'https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_4',
    'Xbox_Series_X/S': 'https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_Series_X_e_Series_S',
    'Xbox_360': 'https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_360',
    'Nintendo_Switch': 'https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Nintendo_Switch'
}

def obter_tabelas_da_wikipedia(url):
    resposta = requests.get(url)
    if resposta.status_code != 200:
        raise Exception(f"Erro ao acessar a URL: {url}")
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    tabelas = sopa.find_all('table', {'class': 'wikitable'})
    return tabelas

def analisar_tabela(tabela):
    cabecalhos = [cabecalho.text.strip() for cabecalho in tabela.find_all('th')]
    linhas = []
    for linha in tabela.find_all('tr')[1:]:
        celulas = linha.find_all(['td', 'th'])
        texto_celulas = [celula.text.strip() for celula in celulas]
        if len(texto_celulas) == len(cabecalhos):
            linhas.append(texto_celulas)
    return cabecalhos, linhas

def limpar_dados(cabecalhos, linhas):
    df = pd.DataFrame(linhas, columns=cabecalhos)
    df = df.replace('\n', '', regex=True).replace('\r', '', regex=True)
    return df

def exportar_dados(df, nome):
    df.to_csv(f'{PATH}{nome}.csv', index=False)
    df.to_json(f'{PATH}{nome}.json', orient='records', lines=True)
    df.to_excel(f'{PATH}{nome}.xlsx', index=False)

for nome, url in urls.items():
    try:
        tabelas = obter_tabelas_da_wikipedia(url)
        if not tabelas:
            print(f"Não foram encontradas tabelas em: {url}")
            continue
        for i, tabela in enumerate(tabelas):
            cabecalhos, linhas = analisar_tabela(tabela)
            df = limpar_dados(cabecalhos, linhas)
            exportar_dados(df, f'{nome}_tabela_{i+1}')
            print(f"Dados da tabela {i+1} de {nome} exportados com sucesso!")
    except Exception as e:
        print(f"Erro ao processar {nome}: {e}")
