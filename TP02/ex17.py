# Simulador de Caixa Eletrônico
# Problema: Desenvolva um programa que simule a operação de um caixa eletrônico, permitindo ao usuário sacar uma quantia especificada e retornando as notas necessárias para o montante.

def caixa_eletronico(valor_saque):
    """
    Simula a operação de um caixa eletrônico, permitindo ao usuário sacar uma quantia especificada e retornar as notas necessárias para o montante.

    Parâmetros:
    - valor_saque: int
        O valor que o usuário deseja sacar do caixa eletrônico.

    Retorno:
    Esta função não retorna nenhum valor. Ela imprime na tela as notas necessárias para o saque, com base nas notas disponíveis no caixa eletrônico.

    Comportamento:
    A função calcula as notas necessárias para o saque do valor especificado pelo usuário, utilizando as seguintes notas disponíveis: 100, 50, 20, 10, 5 e 2 reais. Em seguida, imprime na tela as notas necessárias para o saque ou uma mensagem indicando que não é possível sacar o valor solicitado, caso não seja possível combinar as notas disponíveis para alcançar o valor desejado.
    """
    notas_disponiveis = [100, 50, 20, 10, 5, 2]
    notas_para_saque = {}

    for nota in notas_disponiveis:
        quantidade_notas = valor_saque // nota
        if quantidade_notas > 0:
            notas_para_saque[nota] = quantidade_notas
            valor_saque %= nota

    if valor_saque != 0:
        print("Não é possível sacar o valor solicitado.")
    else:
        print("Notas para o saque:")
        for nota, quantidade in notas_para_saque.items():
            print(f"{quantidade} nota(s) de R${nota},00")

valor = int(input("Digite o valor que deseja sacar: "))
caixa_eletronico(valor)
