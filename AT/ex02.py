# Número 2: Criar um aplicativo que permita ao usuário monitorar suas despesas e receitas, categorizar gastos e visualizar um resumo financeiro.

def mostrar_menu():
    """
    Mostra o menu de opções para o usuário.

    Retorna:
        str: A opção escolhida pelo usuário.
    """
    print("+--------------------------+")
    print("| Monitoramento Financeiro |")
    print("+--------------------------+")

    print("[1] - Adicionar Receita")
    print("[2] - Adicionar Despesa")
    print("[3] - Ver Extrato")
    print("[4] - Relatório de Gastos por Categoria")
    print("[5] - Relatório de Receitas")
    print("[6] - Sair")

    return input("Escolha uma opção: ").replace(',', '.')

class MonitorFinanceiro:
    """
    Classe para realizar o monitoramento financeiro.

    Atributos:
        saldo (float): O saldo atual.
        receitas (list): Lista de tuplas contendo valor e descrição das receitas.
        despesas (list): Lista de tuplas contendo valor, categoria e descrição das despesas.
    """
    
    # Atributos da classe:
    saldo = 0
    receitas = []
    despesas = []

    # Métodos da classe:
    def adicionar_receita(valor, descricao):
        """
        Adiciona uma receita ao saldo e à lista de receitas.

        Args:
            valor (float): O valor da receita.
            descricao (str): Descrição da fonte financeira.
        """
        MonitorFinanceiro.saldo += valor
        MonitorFinanceiro.receitas.append((valor, descricao))

    def adicionar_despesa(valor, categoria, descricao=""):
        """
        Adiciona uma despesa ao saldo e à lista de despesas.

        Args:
            valor (float): O valor da despesa.
            categoria (str): A categoria da despesa.
            descricao (str, opcional): Descrição da despesa.
        """
        MonitorFinanceiro.saldo -= valor
        MonitorFinanceiro.despesas.append((valor, categoria, descricao))

    def extrato():
        """
        Exibe o extrato financeiro mostrando as receitas e despesas.
        """
        print("Extrato Financeiro:")
        if not MonitorFinanceiro.receitas:  # Verifica se a lista está vazia
            print("Nenhum registro até o momento...")
        else:
            saldo_atual = 0
            for receita in MonitorFinanceiro.receitas:
                saldo_atual += receita[0]
                print(f"Receita: +{receita[0]} ({receita[1]}), Saldo: {saldo_atual}")
            for despesa in MonitorFinanceiro.despesas:
                saldo_atual -= despesa[0]
                print(f"Despesa: -{despesa[0]} ({despesa[1]}){' - ' + despesa[2] if despesa[2] else ''}, Saldo: {saldo_atual}")

    def relatorio_gastos_por_categoria():
        """
        Exibe um relatório de gastos por categoria.
        """
        print("Relatório de Gastos por Categoria:")
        if not MonitorFinanceiro.receitas:  # Verifica se a lista está vazia
            print("Nenhum gasto até o momento...")
        else:
            categorias = {}
            for despesa in MonitorFinanceiro.despesas:
                categoria = despesa[1]
                if categoria in categorias:
                    categorias[categoria] += despesa[0]
                else:
                    categorias[categoria] = despesa[0]
            for categoria, total in sorted(categorias.items(), key=lambda x: x[1], reverse=True):
                print(f"{categoria}: {total}")

    def relatorio_receitas():
        """
        Exibe um relatório de receitas.
        """
        print("Relatório de Receitas:")
        if not MonitorFinanceiro.receitas:  # Verifica se a lista está vazia
            print("Nenhuma receita até o momento...")
        else:
            for receita in MonitorFinanceiro.receitas:
                print(f"{receita[0]} ({receita[1]})")


saldo_inicial = float(input("Digite o saldo inicial: ").replace(',', '.'))
MonitorFinanceiro.saldo = saldo_inicial

while True:
    escolha = mostrar_menu()

    if escolha == "1":
        valor = float(input("Digite o valor da receita: ").replace(',', '.'))
        descricao = input("Descreva a fonte financeira: ")
        MonitorFinanceiro.adicionar_receita(valor, descricao)
    elif escolha == "2":
        valor = float(input("Digite o valor da despesa: ").replace(',', '.'))
        categoria = input("Digite a categoria da despesa: ")
        descricao = input("Digite uma descrição (opcional): ")
        MonitorFinanceiro.adicionar_despesa(valor, categoria, descricao)
    elif escolha == "3":
        MonitorFinanceiro.extrato()
    elif escolha == "4":
        MonitorFinanceiro.relatorio_gastos_por_categoria()
    elif escolha == "5":
        MonitorFinanceiro.relatorio_receitas()
    elif escolha == "6":
        print("Fim do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
