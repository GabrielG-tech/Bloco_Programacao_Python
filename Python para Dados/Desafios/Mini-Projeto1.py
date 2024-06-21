import time
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
    """
    Args:
        url (str): A URL da página da Wikipédia a ser acessada.

    Returns:
        list: Uma lista de objetos BeautifulSoup correspondentes às tabelas encontradas na página.
    """
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança exceção para erros HTTP
        soup = BeautifulSoup(resposta.text, 'html.parser')
        tabelas = soup.find_all('table', {'class': 'wikitable'})
        if not tabelas:
            raise Exception("Tabela com classe 'wikitable' não encontrada")
        return tabelas
    
    except requests.exceptions.HTTPError as errh:
        print(f"Erro HTTP: {errh}")
        return None
    
    except requests.exceptions.ConnectionError as errc:
        print(f"Erro de conexão: {errc}")
        return None
    
    except Exception as e:
        print(f"Erro durante o processo de scraping: {e}")
        return None
    

def analisar_tabela(tabela):
    """
    Extrai os cabeçalhos e as linhas de uma tabela HTML.

    Args:
        tabela (BeautifulSoup object): A tabela HTML a ser analisada.

    Returns:
        tuple: Uma tupla contendo a lista de cabeçalhos e a lista de linhas de dados.
    """
    # Extrair os cabeçalhos da tabela
    headers = [header.text.strip() for header in tabela.find_all('th')]

    # Extrair os dados das linhas da tabela
    rows = []
    for row in tabela.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            row_data = [column.text.strip() for column in columns]
            rows.append(row_data)
    return headers, rows


def limpar_dados(headers, linhas):
    """
    Limpa e organiza os dados em um DataFrame do pandas.

    Args:
        headers (list): Lista de cabeçalhos da tabela.
        linhas (list): Lista de linhas de dados da tabela.

    Returns:
        DataFrame: Um DataFrame do pandas com os dados limpos.
    """
    df = pd.DataFrame(linhas, columns=headers)
    df = df.replace('\n', '', regex=True).replace('\r', '', regex=True)

    if 'Título' in df.columns:
        df['Título'] = df['Título'].str.replace('^#', '', regex=True)

    if 'Lançamento' in df.columns:
        df['Lançamento'] = pd.to_datetime(df['Lançamento'], format='%d/%b/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

    if 'Obs.' in df.columns:
        df['Obs.'] = df['Obs.'].str.extract(r'\[(\d+)\]', expand=False)

    if 'Ref.' in df.columns:
        df['Ref.'] = df['Ref.'].str.extract(r'\[(\d+)\]', expand=False)
    
    df.fillna('N/A', inplace=True)
    df.replace('', 'Não definido', inplace=True)
    
    return df

def exportar_dados(df, nome):
    try:
        df.to_csv(f'{PATH}{nome}.csv', index=False)
        df.to_json(f'{PATH}{nome}.json', orient='records', lines=True)
        df.to_excel(f'{PATH}{nome}.xlsx', index=False)
        print(f"Dados de {nome} exportados com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar dados de {nome}: {e}")

# Extração, limpeza e exportação dos dados.
# Percorre todas as URLs, extrai as tabelas, limpa os dados e exporta os resultados.
for nome, url in urls.items():
    try:
        tabelas = obter_tabelas_da_wikipedia(url)
        if not tabelas:
            print(f"Não foram encontradas tabelas em: {url}")
            continue
        for i, tabela in enumerate(tabelas):
            headers, linhas = analisar_tabela(tabela)
            df = limpar_dados(headers, linhas)
            exportar_dados(df, f'{nome}_tabela_{i+1}')
        time.sleep(2)  # Espera de 2 segundos entre requisições para evitar bloqueio
    except Exception as e:
        print(f"Erro ao processar {nome}: {e}")
