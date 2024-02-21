# Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
# Ex: "A cara rajada da jararaca", "A base do teto desaba", "A dama admirou o rim da amada"

palavra = input("Digite uma palavra ou frase: ")

if palavra.lower().replace(" ", "") == palavra[::-1].lower().replace(" ", ""):
    print("Esta palavra é um palíndromo!")
elif palavra.lower().replace(" ", "") != palavra[::-1].lower().replace(" ", ""):
    print("Esta palavra não é um palíndromo!")

print("Palavra ou frase:", palavra[::-1].lower().replace(" ", ""))