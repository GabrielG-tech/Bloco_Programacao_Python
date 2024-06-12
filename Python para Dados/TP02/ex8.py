# Baixe o código do link e execute ele para obter um arquivo fictício de log. Escreva um script que processe esse arquivo de log gerado, tratando-o como um arquivo grande. Crie uma função que filtre as mensagens de erro especificadas no log e salve o timestamp dos erros em um novo arquivo para análise posterior. Crie uma outra função que explore o arquivo log e crie uma lista dos IPs que logaram no sistema e salve em um arquivo ordenado do IP que mais acessou para o IP que menos acessou, registrando a quantidade de loggins logins realizados pelo IP.

import re

def filtrar_erros(arquivo_log, arquivo_saida_erros):
    """
    Filtra mensagens de erro no arquivo de log e salva os timestamps dos erros em um novo arquivo.
    """
    arquivo_log = open(arquivo_log, 'r')
    arquivo_erros = open(arquivo_saida_erros, 'w')
    
    for linha in arquivo_log:
        if "ERROR" in linha:
            timestamp = linha.split(' ')[0]  # Supondo que o timestamp está no início da linha
            arquivo_erros.write(timestamp + '\n')
    
    arquivo_log.close()
    arquivo_erros.close()

def listar_ips(arquivo_log, arquivo_saida_ips):
    """
    Lista os IPs que logaram no sistema e salva em um arquivo ordenado do IP que mais acessou para o IP que menos acessou.
    """
    contagem_ips = {}
    padrao_ip = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    
    arquivo_log = open(arquivo_log, 'r')
    for linha in arquivo_log:
        ip_encontrado = padrao_ip.search(linha)
        if ip_encontrado:
            ip = ip_encontrado.group(0)
            if ip in contagem_ips:
                contagem_ips[ip] += 1
            else:
                contagem_ips[ip] = 1
    arquivo_log.close()

    ips_ordenados = ordenar_por_valor(contagem_ips)

    arquivo_ips = open(arquivo_saida_ips, 'w')
    for ip, contagem in ips_ordenados:
        arquivo_ips.write(f"{ip} {contagem}\n")
    arquivo_ips.close()

def ordenar_por_valor(dicionario):
    """
    Ordena um dicionário por seus valores em ordem decrescente.
    """
    itens = list(dicionario.items())
    for i in range(len(itens)):
        for j in range(i + 1, len(itens)):
            if itens[i][1] < itens[j][1]:
                itens[i], itens[j] = itens[j], itens[i]
    return itens

arquivo_log = 'Python para Dados/TP02/sample_log_file.log'
arquivo_erros = 'Python para Dados/TP02/ex8_erro_timestamps.txt'
arquivo_ips = 'Python para Dados/TP02/ex8_ips_logins.txt'

filtrar_erros(arquivo_log, arquivo_erros)
listar_ips(arquivo_log, arquivo_ips)
