# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y
    
while(True):
    n1 = float(input("Insira o 1º numero: "))
    n2 = float(input("Insira o 2º numero: "))

    operador = input("\n[+] -> Adição\n[-] -> Subtração\n[x] -> Multiplicação\n[/] -> Divisão\n\nEscolha um operador: ")

    if operador == '+':
        print(n1, "+", n2, "=", adicao(n1, n2))
        break
    elif operador == '-':
        print(n1, "-", n2, "=", subtracao(n1, n2))
        break
    elif operador == '*':
        print(n1, "*", n2, "=", multiplicacao(n1, n2))
        break
    elif operador == '/':
        if n2 != 0:
            print(n1, "/", n2, "=", divisao(n1, n2))
            break
        print("Divisão por zero não é permitida, tente outro número.")
    else:
        print("Porfavor selecione uma das opções acima.")

# print("O resultato de " + str(n1) + " " + operador + " " + str(n2) + " é " str(n2))