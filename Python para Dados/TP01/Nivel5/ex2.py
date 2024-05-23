# Nivel 5 - Ex 2
# Dicionários Aninhados: Implemente um programa que manipule um dicionário contendo informações de alunos, onde cada aluno (chave) tem um dicionário com informações das notas em 4 disciplinas que serão inseridas pelo usuário. Quando o programa for encerrado, ele deverá ter gerado dois arquivos, um arquivo com nome “aprovados” e outro com o nome “recuperação” que deverão conter os nomes dos alunos que tiverem média acima ou igual a 6 e os nomes dos alunos com média abaixo de 6, respectivamente.
    
# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Dicionário para armazenar as informações dos alunos
alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    
    # Inicializar o dicionário das disciplinas
    disciplinas = ['Matemática', 'Português', 'História', 'Ciências']
    notas = []
    
    # Coletar as notas das disciplinas
    for disciplina in disciplinas:
        nota = float(input(f"Digite a nota de {disciplina} para {nome}: "))
        notas.append(nota)
    
    # Armazenar as informações do aluno no dicionário
    alunos[nome] = {
        'notas': notas,
        'media': calcular_media(notas)
    }

# Listas para armazenar os nomes dos alunos aprovados e em recuperação
aprovados = []
recuperacao = []

# Classificar os alunos com base na média
for nome, info in alunos.items():
    if info['media'] >= 6:
        aprovados.append(nome)
    else:
        recuperacao.append(nome)

# Gravar os resultados nos arquivos
with open('aprovados.txt', 'w') as file_aprovados:
    for aluno in aprovados:
        file_aprovados.write(f"{aluno}\n")

with open('recuperacao.txt', 'w') as file_recuperacao:
    for aluno in recuperacao:
        file_recuperacao.write(f"{aluno}\n")

print("Processo concluído. Verifique os arquivos 'aprovados.txt' e 'recuperacao.txt'.")

