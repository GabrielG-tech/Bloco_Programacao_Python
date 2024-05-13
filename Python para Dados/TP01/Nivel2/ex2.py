# Nivel 2 - Ex 2
# Leitura de Arquivos CSV: Leia um arquivo CSV e imprima cada linha do arquivo no console.

import csv

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo) # objeto leitor CSV
            for linha in reader:
                print(','.join(linha)) # mostra as linhas como uma única string, separando os elementos por vírgula. 
    except FileNotFoundError:
        print("Arquivo não encontrado.")

nome_do_arquivo = "Python para Dados\\TP01\\Nivel2\\ex2.csv"
ler_arquivo(nome_do_arquivo)


