# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

while(True):
    operador = input("\n[+] -> Adição\n[-] -> Subtração\n[x] -> Multiplicação\n[/] -> Divisão\n\nEscolha um operador: ")

    if (operador == "+"):
        print("Vai")
        break
    elif (operador == "-"):
        print("Catar")
        break
    elif (operador == "-"):
        print("co")
        break
    elif (operador == "-"):
        print("quinho")
        break
    else:
        print("Porfavor selecione uma das opções acima.")

n1 = float(input("Insira o 1º número: "))
n2 = float(input("Insira o 2º número: "))
resultado = 

print("O resultato de " + str(n1) + operador + str(n2) + " é " str(resultado))