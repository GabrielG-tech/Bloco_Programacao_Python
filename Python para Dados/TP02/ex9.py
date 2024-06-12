# Escreva uma função que solicita ao usuário dois números e tenta dividir o primeiro pelo segundo. Use o tratamento de exceções para lidar com a entrada inválida (ex: texto ao invés de número) e a divisão por zero, informando ao usuário a natureza do erro.

def dividir_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 / num2
        except ValueError:
            print("Erro: Por favor, digite valores numéricos válidos.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print(f"O resultado da divisão é: {resultado}")
            break
        
dividir_numeros()
