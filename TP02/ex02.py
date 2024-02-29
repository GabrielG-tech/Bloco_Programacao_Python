# Acumulador de Soma
# Problema: Desenvolva um programa que use um loop while para somar todos os números até 100 e imprimir o resultado.

# Inicialização das variáveis contador e somatório
contador = 0  # Inicia o contador em 0
somatorio = 0  # Inicia o somatório em 0

# Loop while para somar os números até 100
while contador != 100:  # Enquanto o contador não alcançar 100
    contador += 1  # Incrementa o contador em 1 a cada iteração
    somatorio += contador  # Adiciona o valor do contador ao somatório

# Imprime o resultado
print("A soma dos números de 1 a 100 é", somatorio)
