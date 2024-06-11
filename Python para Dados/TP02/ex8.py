# Baixe o código do link e execute ele para obter um arquivo fictício de log. Escreva um script que processe esse arquivo de log gerado, tratando-o como um arquivo grande. Crie uma função que filtre as mensagens de erro especificadas no log e salve o timestamp dos erros em um novo arquivo para análise posterior. Crie uma outra função que explore o arquivo log e crie uma lista dos IPs que logaram no sistema e salve em um arquivo ordenado do IP que mais acessou para o IP que menos acessou, registrando a quantidade de loggins logins realizados pelo IP.

import re
from collections import Counter

# Função para filtrar mensagens de erro e salvar timestamps
def filtrar_erros(logfile, erro_file):
    with open(logfile, 'r') as f, open(erro_file, 'w') as ef:
        for line in f:
            if 'ERROR' in line:
                # Extraindo o timestamp usando regex
                timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line).group()
                ef.write(timestamp + '\n')

# Função para listar IPs e contar logins
def listar_ips(logfile, ip_file):
    ip_counter = Counter()
    with open(logfile, 'r') as f:
        for line in f:
            # Extraindo o IP usando regex
            match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
            if match:
                ip = match.group()
                ip_counter[ip] += 1
    
    # Ordenar IPs pela quantidade de logins (descendente)
    sorted_ips = sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)
    
    with open(ip_file, 'w') as f:
        for ip, count in sorted_ips:
            f.write(f'{ip} {count}\n')

# Arquivos de entrada e saída
logfile = 'Python para Dados\\TP02\\sample_log_file.log'
erro_file = 'Python para Dados\\TP02\\ex8_erro_timestamps.txt'
ip_file = 'Python para Dados\\TP02\\ex8_ips_logins.txt'

# Executar as funções
filtrar_erros(logfile, erro_file)
listar_ips(logfile, ip_file)
