# Número 2: Criar um aplicativo que permita ao usuário monitorar suas despesas e receitas, categorizar gastos e visualizar um resumo financeiro.

def mostrar_menu():
    """
    Mostra o menu de opções para o usuário.
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

def colorirSaldo(saldo):
    """
    Returns uma string formatada de saldo, colorindo de verde se for positivo, vermelho se for negativo e mantendo sem cor se for igual a zero.

    Args:
        saldo (float): O saldo a ser colorido.

    Returns:
        str: Uma string formatada com o saldo colorido (ou não).
    """
    if saldo > 0:
        return f"\033[1;32m{saldo}\033[m" # Pinta de verde
    elif saldo < 0:
        return f"\033[1;31m{saldo}\033[m" # Pinta de vermelho
    else:
        return f"{saldo}"

class MonitorFinanceiro:
    """
    Classe para realizar o monitoramento financeiro.

    Attributes:
        saldo (float): O saldo atual.
        receitas (list): Lista de tuplas contendo valor e descrição das receitas.
        despesas (list): Lista de tuplas contendo valor, categoria e descrição das despesas.

    Methods:
        adicionar_receita(valor, descricao):
            Adiciona uma receita ao saldo e à lista de receitas.

        adicionar_despesa(valor, categoria, descricao=""):
            Adiciona uma despesa ao saldo e à lista de despesas.

        extrato():
            Exibe o extrato financeiro mostrando as receitas e despesas.

        relatorio_gastos_por_categoria():
            Exibe um relatório de gastos por categoria.

        relatorio_receitas():
            Exibe um relatório de receitas.
    """
    saldo = 0
    receitas = []
    despesas = []

    categorias_de_despesa = {
        1: "Alimentação",
        2: "Transporte",
        3: "Moradia",
        4: "Saúde",
        5: "Educação",
        6: "Lazer",
        7: "Outros"
    }

    def mostrar_menu_categorias():
        """
        Mostra o menu de opções de categorias para o usuário.
        """
        print("Escolha a categoria da despesa:")
        for id_categoria, nome_categoria in MonitorFinanceiro.categorias_de_despesa.items():
            print(f"[{id_categoria}] - {nome_categoria}")

    def obter_categoria_despesa():
        """
        Solicita ao usuário a escolha da categoria de despesa e retorna a categoria escolhida válidada.
        
        Returns:
            int: O ID da categoria escolhida.
        """
        while True:
            MonitorFinanceiro.mostrar_menu_categorias()
            try:
                categoria_escolhida = int(input("Digite o número da categoria: "))
                if categoria_escolhida in MonitorFinanceiro.categorias_de_despesa:
                    return categoria_escolhida
                else:
                    print("Categoria inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite apenas números.")

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
                print(f"\033[1;32mReceita: +{receita[0]}\033[m ({receita[1]}), Saldo: {colorirSaldo(saldo_atual)}")
            for despesa in MonitorFinanceiro.despesas:
                saldo_atual -= despesa[0]
                print(f"\033[1;31mDespesa: -{despesa[0]}\033[m ({despesa[1]}){' - ' + despesa[2] if despesa[2] else ''}, Saldo: {colorirSaldo(saldo_atual)}")

    def relatorio_gastos_por_categoria():
        """
        Exibe um relatório de gastos por categoria já pré-definidas.
        """
        print("Relatório de Gastos por Categoria:")
        if not MonitorFinanceiro.despesas:  # Verifica se a lista está vazia
            print("Nenhum gasto até o momento...")
        else:
            categorias = {}
            for despesa in MonitorFinanceiro.despesas:
                valor, categoria, descricao = despesa
                if categoria not in categorias:
                    categorias[categoria] = valor
                else:
                    categorias[categoria] += valor
            
            for categoria, total_gasto in categorias.items():
                print(f"{categoria}: {total_gasto}") # Mostra o somátorio dos gastos por categoria

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

def validar_input_float(mensagem):
    """
    Valida a entrada do usuário para um número decimal (float).

    Args:
        mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        float: O valor inserido pelo usuário.
    """
    while True:
        try:
            entrada = float(input(mensagem).replace(',', '.'))
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def validar_input_inteiro(mensagem):
    """
    Valida a entrada do usuário para um número inteiro.

    Args:
        mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        int: O valor inserido pelo usuário.
    """
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro existente nas opções.")

while True:
    mostrar_menu()
    
    escolha = validar_input_inteiro("Escolha uma opção: ")

    if escolha == 1:
        valor = validar_input_float("Digite o valor da receita: ")
        descricao = input("Descreva a fonte financeira: ")
        MonitorFinanceiro.adicionar_receita(valor, descricao)
    elif escolha == 2:
        categoria_escolhida = MonitorFinanceiro.obter_categoria_despesa()
        valor = validar_input_float("Digite o valor da despesa: ")
        descricao = input("Digite a descrição (opcional): ")
        MonitorFinanceiro.adicionar_despesa(valor, categoria_escolhida, descricao)
    elif escolha == 3:
        MonitorFinanceiro.extrato()
    elif escolha == 4:
        MonitorFinanceiro.relatorio_gastos_por_categoria()
    elif escolha == 5:
        MonitorFinanceiro.relatorio_receitas()
    elif escolha == 6:
        print("Fim do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")