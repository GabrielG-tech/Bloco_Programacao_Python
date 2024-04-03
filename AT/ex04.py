# Número 4: Criar um programa que gere senhas fortes aleatoriamente, com comprimento definido pelo usuário e as armazene em uma estrutura de dados criptografada.

import sqlite3
import os

PALAVRA_CHAVE = "segredo"  # Palavra-chave para acesso à consulta
CHAVE_CRIPTOGRAFIA = 3  # Chave para a cifra de César
DATABASE_PATH = "AT/dados.db"  # Caminho para o banco de dados SQLite

def cifra_cesar(texto, chave):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            novo_char = chr((ord(char) - ord('a' if char.islower() else 'A') + chave) % 26 + ord('a' if char.islower() else 'A'))
            texto_cifrado += novo_char
        else:
            texto_cifrado += char
    return texto_cifrado

def gerar_senha(comprimento):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    senha = ''.join(cifra_cesar(char, CHAVE_CRIPTOGRAFIA) for char in caracteres[:comprimento])
    return senha

def criar_tabela():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Senhas
                      (nome_servico TEXT, username TEXT, senha TEXT)''')
    conn.commit()
    conn.close()

def criptografar_dados(dados):
    return cifra_cesar(dados, CHAVE_CRIPTOGRAFIA)

def descriptografar_dados(dados_cifrados):
    return cifra_cesar(dados_cifrados, -CHAVE_CRIPTOGRAFIA)

def salvar_dados(nome_servico, username, senha):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Senhas VALUES (?, ?, ?)", (nome_servico, username, senha))
    conn.commit()
    conn.close()

def consultar_dados():
    palavra_chave = input("Digite a palavra-chave para acesso à consulta: ")
    if palavra_chave != PALAVRA_CHAVE:
        print("Palavra-chave incorreta.")
        return
    
    nome_servico = input("Digite o nome do serviço: ")

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Senhas WHERE nome_servico = ?", (nome_servico,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print(f"Username: {resultado[1]}")
        print(f"Senha: {resultado[2]}")
    else:
        print("Serviço não encontrado.")

# Verifica se a pasta "AT" existe, se não existir, cria-a
if not os.path.exists("AT"):
    os.makedirs("AT")

# Cria a tabela no banco de dados
criar_tabela()

opcao = input("[1] Gerar senha\n[2] Consultar senha\nEscolha uma opção: ")

if opcao == "1":
    nome_servico = input("Digite o nome do serviço: ")
    username = input("Digite o username: ")
    comprimento = int(input("Digite o comprimento da senha desejado: "))
    senha = gerar_senha(comprimento)
    salvar_dados(nome_servico, username, senha)
    print("Senha gerada e salva com sucesso!")
elif opcao == "2":
    consultar_dados()
else:
    print("Opção inválida.")