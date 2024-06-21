import time
from urllib import request
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
    Faz uma requisição HTTP para uma URL da Wikipédia e retorna todas as tabelas com a classe 'wikitable'.

    Args:
        url (str): A URL da página da Wikipédia a ser acessada.

    Returns:
        list: Uma lista de objetos BeautifulSoup correspondentes às tabelas encontradas na página.
    """
    try:
        resposta = requests.get(url, headers={'User-Agent': 'Googlebot'})
        resposta.raise_for_status()  # Lança uma exceção para erros HTTP (4xx/5xx)
        
        conteudo = resposta.content
        soup = BeautifulSoup(conteudo, 'html.parser')
        tabelas = soup.find_all('table', {'class': 'wikitable'})
        
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
    # req = request.Request(url, headers={'User-Agent': 'Googlebot'})
    # with request.urlopen(req) as response:
    #     if response.status != 200:
    #         raise Exception(f"Erro ao acessar a URL: {url}")
    #     conteudo = response.read().decode('utf-8')
    # soup = BeautifulSoup(conteudo, 'html.parser')
    # tabelas = soup.find_all('table', {'class': 'wikitable'})
    # return tabelas

def analisar_tabela(tabela):
    """
    Extrai os cabeçalhos e as linhas de uma tabela HTML.

    Args:
        tabela (BeautifulSoup object): A tabela HTML a ser analisada.

    Returns:
        tuple: Uma tupla contendo a lista de cabeçalhos e a lista de linhas de dados.
    """
    headers = [header.text.strip() for header in tabela.find_all('th')]
    linhas = []
    for linha in tabela.find_all('tr')[1:]:
        celulas = linha.find_all(['td', 'th'])
        texto_celulas = [celula.text.strip() for celula in celulas]
        if len(texto_celulas) == len(headers):
            linhas.append(texto_celulas)
    return headers, linhas

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

    # Remover '#' do início dos títulos
    df['Título'] = df['Título'].str.replace('^#', '', regex=True)

    # Formatar coluna de data para AAAA-MM-DD
    df['Lançamento'] = pd.to_datetime(df['Lançamento'], format='%d/%b/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

    # Limpar campos numéricos como Observações (Obs.) e Referências (Ref.)
    df['Obs.'] = df['Obs.'].str.extract(r'\[(\d+)\]', expand=False)
    df['Ref.'] = df['Ref.'].str.extract(r'\[(\d+)\]', expand=False)
    
    # Substituir valores vazios por 'N/A'
    df.fillna('N/A', inplace=True)
    return df

def exportar_dados(df, nome):
    """
    Exporta os dados do DataFrame para arquivos CSV, JSON e Excel.

    Args:
        df (DataFrame): O DataFrame a ser exportado.
        nome (str): Nome base para os arquivos exportados.
    """
    df.to_csv(f'{PATH}{nome}.csv', index=False, encoding='utf-8')
    df.to_json(f'{PATH}{nome}.json', orient='records', lines=True, encoding='utf-8')
    df.to_excel(f'{PATH}{nome}.xlsx', index=False, encoding='utf-8')

# Extração, limpeza e exportação dos dados.
# # Percorre todas as URLs, extrai as tabelas, limpa os dados e exporta os resultados.
for nome, url in urls.items():
    try:
        tabelas = obter_tabelas_da_wikipedia(url)
        if not tabelas:
            print(f"Não foram encontradas tabelas em: {url}")
            continue
        for i, tabela in enumerate(tabelas):
            headers, linhas = analisar_tabela(tabela)
            if len(headers) >= 2 and len(linhas) >= 2:
                df = limpar_dados(headers, linhas)
                exportar_dados(df, f'{nome}_tabela_{i+1}')
                print(f"Dados da tabela {i+1} de {nome} exportados com sucesso!")
            else:
                print(f"Tabela {i+1} de {nome} não atende aos requisitos mínimos e foi ignorada.")
        time.sleep(2)  # Espera de 2 segundos entre requisições para evitar bloqueio
    except Exception as e:
        print(f"Erro ao processar {nome}: {e}")
