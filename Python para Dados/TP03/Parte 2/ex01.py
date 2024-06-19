# Escreva uma função que solicita ao usuário dois números e tenta dividir o primeiro pelo segundo. Use tratamento de exceções para lidar com os possíveis erros como: a entrada inválida (ex: texto ao invés de número), conversão de tipo, a divisão por zero e outros que você considere pertinente, informando ao usuário a natureza do erro e lidando com cada de uma forma diferente.

def dividir_numeros():
    """
    Solicita 2 números e tenta dividir o 1º pelo 2º, com tratamento de exceções:
    - ValueError: Informar o usuário que a entrada deve ser numérica.
    - ZeroDivisionError: Informar o usuário que a divisão por zero não é permitida.
    - Exception: Informar o usuário de qualquer outro erro inesperado que possa ocorrer.

    A função continua solicitando a entrada até que uma divisão válida seja realizada.
    """
    while True:
        try:
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            num1 = float(num1)
            num2 = float(num2)
            
            resultado = num1 / num2
            
            print(f"O resultado da divisão de {num1} por {num2} é: {resultado}")
            break

        except ValueError:
            print("Erro: Você digitou um valor inválido. Por favor, digite apenas números.")
            
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida. Por favor, digite um segundo número diferente de zero.")
        
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
