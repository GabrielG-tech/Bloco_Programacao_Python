# Nivel 5 - Ex 2
# Dicionários Aninhados: Implemente um programa que manipule um dicionário contendo informações de alunos, onde cada aluno (chave) tem um dicionário com informações das notas em 4 disciplinas que serão inseridas pelo usuário. Quando o programa for encerrado, ele deverá ter gerado dois arquivos, um arquivo com nome “aprovados” e outro com o nome “recuperação” que deverão conter os nomes dos alunos que tiverem média acima ou igual a 6 e os nomes dos alunos com média abaixo de 6, respectivamente.

def inserir_dados_alunos():
    alunos = {}
    
    # Pergunta o nome das disciplinas uma vez e reaproveita para os demais alunos
    disciplinas = []
    for i in range(4):
        while True:
            try:
                disciplina = input(f"Digite o nome da disciplina {i+1}: ").strip().capitalize()
                if not disciplina.isalpha():
                    raise ValueError("O nome da disciplina deve conter apenas letras.")
                disciplinas.append(disciplina)
                break
            except ValueError as e:
                print(e)
    
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para terminar): ").strip().capitalize()
        if nome.lower() == 'sair':
            break
        if not nome.isalpha():
            print("O nome do aluno deve conter apenas letras.")
            continue
        notas = {}
        for disciplina in disciplinas:
            while True:
                try:
                    nota = float(input(f"Digite a nota de {nome} em {disciplina}: ").strip())
                    if nota < 0 or nota > 10:
                        raise ValueError("A nota deve estar entre 0 e 10.")
                    notas[disciplina] = nota
                    break
                except ValueError as e:
                    print(e)
        alunos[nome] = notas
    return alunos

def calcular_media(notas):
    return sum(notas.values()) / len(notas)

def classificar_alunos(alunos):
    aprovados = []
    recuperacao = []
    for aluno, notas in alunos.items():
        media = calcular_media(notas)
        if media >= 6:
            aprovados.append(aluno)
        else:
            recuperacao.append(aluno)
    return aprovados, recuperacao

def salvar_arquivos(aprovados, recuperacao):
    aprovados_path = "Python para Dados/TP01/Nivel5/aprovados.txt"
    recuperacao_path = "Python para Dados/TP01/Nivel5/recuperacao.txt"

    with open(aprovados_path, "w", encoding='utf-8') as aprovados_file:
        for aluno in aprovados:
            aprovados_file.write(f"{aluno}\n")
    
    with open(recuperacao_path, "w", encoding='utf-8') as recuperacao_file:
        for aluno in recuperacao:
            recuperacao_file.write(f"{aluno}\n")

alunos = inserir_dados_alunos()
aprovados, recuperacao = classificar_alunos(alunos)
salvar_arquivos(aprovados, recuperacao)
print("Dados salvos nos arquivos 'aprovados.txt' e 'recuperacao.txt'.")
