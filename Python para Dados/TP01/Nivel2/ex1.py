# Nivel 2 - Ex 1
# Leitura de Arquivos: Escreva um programa que lê um arquivo de texto e imprime seu conteúdo linha por linha.

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readline()
            while linha:
                print(linha.strip())
                linha = arquivo.readline()
    except FileNotFoundError:
        print("Arquivo não encontrado.")

nome_do_arquivo = "Python para Dados\\TP01\\Nivel2\\ex1.txt"
ler_arquivo(nome_do_arquivo)
