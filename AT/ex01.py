# Número 1: Objetivo: Criar um jogo de perguntas e respostas (trivia), no qual os jogadores respondem questões de múltipla escolha. 

import random

# Banco de perguntas e respostas
perguntas = [
    {
        "pergunta": "Qual é a linguagem de programação mais usada para desenvolvimento web?",
        "opcoes": ["a) Python", "b) Java", "c) JavaScript", "d) C#"],
        "resposta": "c"
    },
    {
        "pergunta": "O que é um 'loop for' em Python?",
        "opcoes": ["a) Um loop que executa uma quantidade fixa de vezes", "b) Um loop que nunca termina", "c) Um loop que executa apenas uma vez", "d) Um loop que não faz nada"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é o operador lógico 'OU' em Python?",
        "opcoes": ["a) ||", "b) OR", "c) &&", "d) AND"],
        "resposta": "b"
    },
    {
        "pergunta": "O que é um 'bug' em programação?",
        "opcoes": ["a) Uma característica não intencional de um programa", "b) Um erro lógico em um programa", "c) Uma peça de hardware defeituosa", "d) Um tipo de inseto virtual"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é o resultado da expressão 3 + 2 * 4 em Python?",
        "opcoes": ["a) 20", "b) 15", "c) 11", "d) 14"],
        "resposta": "c"
    },
    {
        "pergunta": "O que é uma 'variável' em programação?",
        "opcoes": ["a) Um valor fixo que não pode ser alterado", "b) Um tipo de operador matemático", "c) Um contêiner para armazenar dados", "d) Uma instrução de controle de fluxo"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual é a estrutura de dados que armazena pares chave-valor?",
        "opcoes": ["a) Lista", "b) Tupla", "c) Dicionário", "d) Conjunto"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual é a diferença entre '==' e '===' em JavaScript?",
        "opcoes": [
            "a) '===' compara o valor e o tipo de dados estritamente, enquanto '==' compara apenas o valor",
            "b) '===' compara apenas o valor, enquanto '==' compara o valor e o tipo de dados estritamente",
            "c) '===' e '==' são equivalentes e não há diferença entre eles",
            "d) '===' e '==' são operadores para atribuição e não para comparação de valores"
        ],
        "resposta": "a"
    },
    {
        "pergunta": "O que é um 'loop while' em programação?",
        "opcoes": [
            "a) Um loop que executa uma quantidade fixa de vezes",
            "b) Um loop que executa apenas uma vez",
            "c) Um loop que continua a executar enquanto uma condição é verdadeira",
            "d) Um loop que não faz nada"
        ],
        "resposta": "c"
    },
    {
        "pergunta": "O que é 'CSS'?",
        "opcoes": [
            "a) Uma linguagem de programação usada para criar páginas web dinâmicas",
            "b) Uma linguagem de marcação para estruturar o conteúdo das páginas web",
            "c) Um sistema de gerenciamento de banco de dados para armazenar informações de estilo",
            "d) Uma linguagem de estilo utilizada para definir a apresentação visual das páginas web"
        ],
        "resposta": "d"
    },
    {
        "pergunta": "Qual é a função do operador '!=' em Python?",
        "opcoes": ["a) Igualdade", "b) Diferença", "c) Menor que", "d) Maior que"],
        "resposta": "b"
    },
    {
        "pergunta": "O que é um 'argumento' em programação?",
        "opcoes": ["a) Um tipo de erro", "b) Um valor fixo que não pode ser alterado", "c) Um valor passado para uma função", "d) Uma estrutura de controle de fluxo"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual é o resultado da expressão '3' + '2' em JavaScript?",
        "opcoes": ["a) 5", "b) '32'", "c) '5'", "d) 32"],
        "resposta": "b"
    },
    {
        "pergunta": "O que é um 'framework' em programação?",
        "opcoes": ["a) Uma ferramenta para depuração de código", "b) Uma linguagem de programação", "c) Uma estrutura para desenvolvimento de software", "d) Um tipo de arquivo"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual é o símbolo usado para concatenar strings em Python?",
        "opcoes": ["a) +", "b) -", "c) *", "d) /"],
        "resposta": "a"
    }
]

# Perguntas utilizadas nas rodada anteriores
perguntas_utilizadas = []

def mostra_pergunta(pergunta):
    """
    Exibe uma pergunta e suas opções.

    Args:
    pergunta (dict): Um dicionário com os tópicos a pergunta, opções e resposta.
    """
    print("•", pergunta["pergunta"])
    [print(opcao) for opcao in pergunta["opcoes"]]

def analisa_resposta(pergunta, resposta):
    """
    Verifica e sinaliza se a resposta do jogador está correta, caso não esteja, diz qual é a certa.

    Args:
    pergunta (dict): Um dicionário com os tópicos a pergunta, opções e resposta.
    resposta (str): A resposta fornecida pelo jogador.

    Returns:
    bool: Retorna True se a resposta estiver correta e False caso não esteja correta.
    """
    if resposta == pergunta["resposta"]:
        print("\033[32;1mResposta correta!\033[0m\n")
        return True
    else:
        print("\033[31;1mResposta incorreta.\033[0m A resposta correta era:\033[1m", pergunta["resposta"].upper(), "\033[0m\n")
        return False

def selecionar_perguntas():
    """
    Seleciona 5 perguntas diferentes das utilizadas na rodada anterior.

    Returns:
    list: Uma lista contendo as perguntas selecionadas.
    """
    perguntas_disponiveis = [pergunta for pergunta in perguntas if pergunta not in perguntas_utilizadas]
    if len(perguntas_disponiveis) == 0:
        return "Sem mais questões"
    else:
        return random.sample(perguntas_disponiveis, min(5, len(perguntas_disponiveis))) # Caso tenha menos de 5 questões disponíveis ele usa as restantes

def titulo(mensagem = "Seja Bem-Vindo(a) ao \033[1mTrivia do Código\033[0m"):
        """
        Imprime o título da Trivia do Código.
        """
        print("+-" + "-"*(len(mensagem)-8) + "-+")
        print(f"| {mensagem} |")
        print("+-" + "-"*(len(mensagem)-8) + "-+")

def jogo_trivia(pontuacao_total=0, num_rodada=1):
    """
    Executa o jogo trivia.

    Controla a pontuação do jogador, exibe perguntas, processa respostas
    e inicia uma nova rodada se o jogador acertar todas as perguntas.

    Args:
    pontuacao_total (int): A pontuação total acumulada até o momento.

    Returns:
    int: A pontuação total de todas as rodadas.
    """
    pontuacao = 0
    perguntas_rodada = selecionar_perguntas() 

    # Adiciona as perguntas usadas na rodada anterior a um outro dicionário para evitar repetições
    perguntas_utilizadas.extend(perguntas_rodada)
    
    if perguntas_rodada == "Sem mais questões":
        titulo("\033[1mParabéns\033[0m")
        print("Parabéns!! \033[1mVocê zerou o jogo!\033[0m Não há mais perguntas disponíveis.")
        return pontuacao_total
    
    
    titulo(f"\033[1m{num_rodada}º Rodada\033[0m")
    num_rodada += 1

    for pergunta in perguntas_rodada:
        mostra_pergunta(pergunta)
        resposta = input("Escolha a alternativa correta (a, b, c ou d): ").lower()
        if analisa_resposta(pergunta, resposta):
            pontuacao += 1
        else:
            break
    print("Pontuação da rodada:", pontuacao)
    
    pontuacao_total += pontuacao

    if pontuacao == 5:
        print("Parabéns! Você acertou todas as perguntas. Iniciando uma nova rodada...\n")
        return jogo_trivia(pontuacao_total, num_rodada)
    return pontuacao_total

titulo()
pontuacao_total = jogo_trivia()
print("O somatório da sua pontuação de todas as rodadas foi de\033[1m", pontuacao_total, "pontos!\033[0m")