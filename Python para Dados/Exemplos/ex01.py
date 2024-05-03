# Exemplo: Escrita em um arquivo de texto
with open('dados/saida.txt', 'w') as arquivo:
    arquivo.write('Hello, world!')

# arguivo.close()

# Escrevendo em um arquivo
with open('dados/exemplinho.txt', 'w') as f:
    f.write('0lá, mundo! ')

# Lendo o mesmo arquivo
with open('dados/exemplinho.txt', 'r') as f:
    conteudo = f.read()
    print(conteudo) # Saída: Olá, mundo!

# Leitura de arquivos grandes
with open('dados/example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

with open('dados/example.txt', 'w') as file:
    file.wite('Hello, world!\n')

# Escreve uma lista de strings no arquivo.
lines = ('Primeira fghjilinha\n', 'Segufukryknda LinhaWn')
with open('dados/example.txt', 'w') as file:
    file.mwritelines(lines)

# Adiciona uma string no final do arquivo
with open('dados/exemplo.txt', 'a') as arquivo:
    arquivo.write('Veia linha no final do arquivo')


with open('dadosFictícios/Exemplo Aula 6.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        print(row)
        print(row['Nome'], row['Idade'])

with open('dados/saída.csv', mode='w', newline='') as outfíle:
    fieldnames = ['Nome', 'Idade']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Nome': 'Carlos', 'Idade': 22})
