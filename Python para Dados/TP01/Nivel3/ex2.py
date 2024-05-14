# Nivel 3 - Ex 2
# Conversão de CSV para JSON: Desenvolva um programa Python que leia um arquivo CSV contendo as colunas nome, idade e email, e converta esses dados para o formato JSON. O resultado deve ser salvo em um novo arquivo JSON. Utilize as bibliotecas csv e json para realizar a leitura e a escrita dos dados, respectivamente.

from csv import DictReader
from json import dump

def csv_para_json(nome_arquivo_csv, nome_arquivo_json):
    dados = []

    # lê o arquivo CSV
    try:
        with open(nome_arquivo_csv, newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = DictReader(arquivo_csv)  # le as linhas como dicionários
            for linha in leitor_csv:
                dados.append(linha)
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
        return

    # escreve os dados (da lista) no arquivo JSON
    try:
        with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
            dump(dados, arquivo_json, indent=4, ensure_ascii=False)  # escreve os dados no JSON
    except IOError:
        print("Erro ao escrever arquivo JSON.")
        return
    
    print("Conversão de CSV para JSON concluída!")
