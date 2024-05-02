# Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

banana = 0
maca = 0
pera = 0

continuar = "s"
while(continuar != "n"):
    print("\n")
    print("="*8, "[Votação] O que você refere?","="*3)
    print("[1] - Banana")
    print("[2] - Maçã")
    print("[3] - Pera")

    voto = int(input("Voto: "))
    if (voto != 1 and voto != 2 and voto != 3):
        print("Votação inválida, tente novamente.")
    elif (voto == 1):
        banana += 1 
        print("Votação computada com sucesso!")
    elif (voto == 2):
        maca += 1 
        print("Votação computada com sucesso!")
    elif (voto == 3):
        pera += 1 
        print("Votação computada com sucesso!")
    continuar = input("Deseja vota novamente? [s/n]: ").lower()
print("\n")
print("="*8, "Resultados","="*8)
print("Banana:\t", banana)
print("Maçã:\t", maca)
print("Pera:\t", pera)
