# Conversor de Temperatura
# Problema: Implemente uma função que converta a temperatura de Celsius para Fahrenheit.

def celsius_para_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit.

    Args:
        celsius (float): A temperatura em graus Celsius a ser convertida.

    Returns:
        float: A temperatura equivalente em graus Fahrenheit.
    """
    # Fórmula de conversão de Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicita ao usuário para inserir a temperatura em Celsius
temperatura_celsius = float(input("Insira uma temperatura em Celsius (Cº): ").replace(",", "."))

# Chama a função para converter a temperatura
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Imprime o resultado
print("{}ºC equivale a {}ºF".format(temperatura_celsius, temperatura_fahrenheit))
