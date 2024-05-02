# "O Jogode Adivinhação”

# Crie um jogo de adivinhação onde o computador escolhe um número entre 1 e 100, é usuário tem que adivinhar o número. O programa deve informar se o palpite do usuário é muito alto, muito baixo, ou correto. Além disso, 0 jogo deve limitar o número de tentativas do usuário.

# Para gerar um número aleatório inclua o seguinte no início do código:
import random
numero_secreto = random.randint(1, 3)
numero_de_tentativas = 0

tentativa = int(input("Tente adivinha o número que estou pensando: "))

while (True):
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou, eu realmente estava pensando no número", numero_secreto)
        break
    elif tentativa != numero_secreto:
        tentativa = int(input("Oh não! Você errou, tente novamente: "))
        numero_de_tentativas += 1

# numeroc = int(input("Escolha um numero de 1 a 100: "))
# tentativas =5
# rodada =1

# while (rodada <= tentativas):
#     input_usuario = int(input("Que número estou pensando: "))
# if numeroc == numero_secreto:
#  print("Está correto")
# if numeroc > numero_secreto:
#    print("Está muito alto")
# if numeroc < numero_secreto:
#     print(" Está muito baixo")