# Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

from random import randrange
print(51*"=" + "\n\t\t  Jogo de adivinhar\n" + 51*"=")

print("[1] - Fácil")
print("[2] - Médio")
print("[3] - Difícil")
print("[4] - INSANO")

dificuldade = int(input("Escolha o nível de dificuldade: "))

if dificuldade == 1:
    n = randrange(0,9)
    vidas = 6
    tentativa = int(input("Tente adivinha que número estou pensando [0-9]: "))
elif dificuldade == 2:
    n = randrange(0,49)
    vidas = 24
    tentativa = int(input("Tente adivinha que número estou pensando [0-49]: "))
elif dificuldade == 3:
    n = randrange(0,100)
    vidas = 49
    tentativa = int(input("Tente adivinha que número estou pensando [0-100]: "))
elif dificuldade == 4:
    n = randrange(0,100000)
    vidas = 99
    tentativa = int(input("Tente adivinha que número estou pensando [0-100000]: "))


while(vidas != 0):
    if (tentativa > n):
        print("\nVocê tem", vidas, "vidas!")    
        tentativa = int(input("Muito alto\nTente de novo: "))
        vidas -= 1
    elif (tentativa < n):
        print("\nVocê tem", vidas, "vidas!")   
        tentativa = int(input("Muito baixo\nTente de novo: "))
        vidas -= 1
    elif (tentativa == n):
        print("Parabés você acertou, o número que eu pensei era", n, "mesmo!")
        break

if (vidas == 0):
    print("Suas vidas acabaram, você perdeu!")