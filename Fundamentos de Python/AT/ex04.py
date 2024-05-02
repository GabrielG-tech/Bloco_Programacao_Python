# Número 4: Criar um programa que gere senhas fortes aleatoriamente, com comprimento definido pelo usuário e as armazene em uma estrutura de dados criptografada.

import sqlite3
import random

PALAVRA_CHAVE = "segredo"  # Palavra-chave para acesso à consulta
CHAVE_CRIPTOGRAFIA = 3  # Chave para a cifra de César
DATABASE_PATH = "AT/dados.db"  # Caminho para o banco de dados SQLite

import random

def cifra_cesar(mensagem, chave=CHAVE_CRIPTOGRAFIA):
    """
    Codifica uma mensagem usando a cifra de César.

    Args:
        mensagem (str): Uma mensagem a ser codificada.
        chave (int): O número de posições para deslocar no alfabeto.

    Returns:
        str: Mensagem codificada.
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem_codificada = ''

    for caractere in mensagem:
        if caractere.isalpha():
            indice = alfabeto.index(caractere)
            novo_indice = (indice + chave) % len(alfabeto)
            novo_caractere = alfabeto[novo_indice]
            mensagem_codificada += novo_caractere
        else:
            mensagem_codificada += caractere # Caso o não seja uma letra, mantém o caractere original
    return mensagem_codificada

def gerar_senha(comprimento=4):
    """
    Gera uma senha aleatória com letras (maiúsculas e minúsculas), números e símbolos.

    Args:
        comprimento (int): O comprimento da senha a ser gerada.

    Returns:
        str: A senha aleatória gerada.
    """
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+~|}{[]:;?><,./-='
    senha = []

    senha.extend([
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ])

    for _ in range(comprimento - 4):
        resto_da_senha = random.choice([letras_maiusculas, letras_minusculas, numeros, simbolos])
        senha.append(random.choice(resto_da_senha))

    # Embaralha a senha
    random.shuffle(senha)

    # Converte a lista de caracteres em uma string
    senha = ''.join(senha)
    return cifra_cesar(senha)

def criar_tabela():
    """
    Cria uma tabela no banco de dados SQLite para armazenar senhas, caso ela não exista.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Senhas
                      (nome_servico_criptografado TEXT, nome_servico TEXT, username TEXT, senha TEXT)''')
    conn.commit()
    conn.close()


def criptografar_dados(dados):
    """
    Criptografa os dados usando a cifra de César.

    Args:
        dados (str): Os dados a serem criptografados.

    Returns:
        str: Dados criptografados.
    """
    return cifra_cesar(dados, CHAVE_CRIPTOGRAFIA)

def descriptografar_dados(dados_cifrados):
    """
    Descriptografa os dados cifrados usando a cifra de César.

    Args:
        dados_cifrados (str): Os dados cifrados a serem descriptografados.

    Returns:
        str: Dados descriptografados.
    """
    return cifra_cesar(dados_cifrados, -CHAVE_CRIPTOGRAFIA)

def salvar_dados(nome_servico, username, senha):
    """
    Salva os dados (nome do serviço, username e senha) na tabela Senhas do banco de dados.

    Args:
        nome_servico (str): O nome do serviço.
        username (str): O username associado ao serviço.
        senha (str): A senha associada ao serviço.
    """
    nome_servico_criptografado = criptografar_dados(nome_servico)
    username_criptografado = criptografar_dados(username)
    senha_criptografada = criptografar_dados(senha)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Senhas VALUES (?, ?, ?, ?)", (nome_servico_criptografado, nome_servico, username_criptografado, senha_criptografada))
    conn.commit()
    conn.close()

def consultar_dados():
    """
    Consulta os dados de um serviço específico na tabela Senhas do banco de dados.
    """    
    nome_servico = input("Digite o nome do serviço: ")
    palavra_chave = input("Digite a palavra-chave para acesso à consulta: ")
    if palavra_chave != PALAVRA_CHAVE:
        print("Palavra-chave incorreta.")
        return
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Senhas WHERE nome_servico = ?", (nome_servico,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        username_criptografado = resultado[2]
        senha_criptografada = resultado[3]
        username = descriptografar_dados(username_criptografado)
        senha = descriptografar_dados(senha_criptografada)
        print(f"Username: {username}")
        print(f"Senha: {senha}")
    else:
        print("Serviço não encontrado.")


def validar_input_inteiro(mensagem):
    """
    Valida a entrada do usuário para um número inteiro.

    Args:
        mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        int: O valor inserido pelo usuário.
    """
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro existente nas opções.")

# Cria a tabela no banco de dados (caso ela não exista)
criar_tabela()

print("+--------------------------------------------------+")
print("| \033[3mBem-vindo(a) ao Gerador e Gerenciador de Senhas!\033[m |")
print("+--------------------------------------------------+")

while True:
    print("[1] Gerar senha")
    print("[2] Consultar senha")
    print("[3] Finalizar programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_servico = input("Digite o nome do serviço: ")
        username = input("Digite o username: ")
        comprimento = validar_input_inteiro("Digite o comprimento da senha desejado: ")
        senha = gerar_senha(comprimento)
        salvar_dados(nome_servico, username, senha)
        print("Senha gerada e salva com sucesso!")
    elif opcao == "2":
        consultar_dados()
    elif opcao == "3":
        print("Fim do programa.")
        exit()
    else:
        print("Opção inválida.")