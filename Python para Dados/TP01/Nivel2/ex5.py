# Nivel 2 - Ex 5
# Escrita em Arquivos JSON: Escreva um programa que colete dados do usuário, os salve em um dicionário e então escreva esse dicionário em um arquivo no formato JSON.

import json

def coletar_dados_usuario():
    dados = {}
    dados['nome'] = input("Digite seu nome: ")
    dados['idade'] = int(input("Digite sua idade: "))
    dados['email'] = input("Digite seu email: ")
    return dados

def salvar_json(nome_arquivo, novo_dado):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {}

    proximo_id = str(len(dados) + 1) # gera um id para cada pessoa. pega o tamanho atual do dic e add 1.
    dados[proximo_id] = novo_dado # add os dados do novo usuário ao dic, usando o id como chave.

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4) # Escreve json formatado de maneira que fique mais legivel

nome_arquivo = "Python para Dados\\TP01\\Nivel2\\ex5.json"

dados_usuario = coletar_dados_usuario()
salvar_json(nome_arquivo, dados_usuario)
print("Dados do usuário foram adicionados ao arquivo com sucesso!")
