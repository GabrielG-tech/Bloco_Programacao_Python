from tkinter import *

def centralizar_janela(janela, largura=300, altura=350):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    janela.geometry('{}x{}+{}+{}'.format(largura, altura, pos_x, pos_y))

def sudoku_janela():
    nova_janela = Toplevel(root)
    centralizar_janela(nova_janela, 400, 400)
    nova_janela.title("Sudoku")
    
    # Criando um frame para os widgets
    frame = Frame(nova_janela, bg="green")
    frame.pack(expand=True, fill=BOTH)

    # Entry para o Sudoku
    quadradoEntry = Entry(frame, width=5, font=("Verdana", 20))
    quadradoEntry.pack(padx=5, pady=5)

def jogo_da_velha_janela():
    nova_janela = Toplevel(root)
    centralizar_janela(nova_janela, 400, 420)
    nova_janela.title("Jogo da Velha")
    
    # Criando um frame para os widgets
    frame = Frame(nova_janela, bg="gray")
    frame.pack(pady=10)

    # Variáveis globais para o Jogo da Velha
    global jogador_atual, tabuleiro
    jogador_atual = "X"
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Função para lidar com o clique em um botão do tabuleiro
    def clicar_botao(linha, coluna):
        # Verificar se a célula está vazia
        if tabuleiro[linha][coluna] == " ":
            # Atualizar o texto do botão com a jogada do jogador atual
            botoes[linha][coluna].config(text=jogador_atual)
            tabuleiro[linha][coluna] = jogador_atual
            trocar_jogador()
            verificar_resultado()

    def trocar_jogador():
        global jogador_atual
        jogador_atual = "X" if jogador_atual == "O" else "O"

    def verificar_resultado():
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
                mostrar_vencedor(tabuleiro[i][0])
            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
                mostrar_vencedor(tabuleiro[0][i])
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            mostrar_vencedor(tabuleiro[0][0])
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            mostrar_vencedor(tabuleiro[0][2])
        # Verificar empate
        if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
            mostrar_vencedor("Empate")

    def mostrar_vencedor(vencedor):
        if vencedor == "Empate":
            vencedor_texto = "Deu Velha!"
        else:
            vencedor_texto = f"O jogador {vencedor} venceu!"
        vencedor_label = Label(nova_janela, text=vencedor_texto, font=("Verdana", 20), bg="gray")
        vencedor_label.pack(pady=10)

    # Criar e posicionar os botões do tabuleiro
    botoes = []
    for i in range(3):
        linha_botoes = []
        for j in range(3):
            botao = Button(frame, text=" ", font=("Verdana", 20), width=4, height=2,
                           command=lambda linha=i, coluna=j: clicar_botao(linha, coluna))
            botao.grid(row=i, column=j, padx=5, pady=5)
            linha_botoes.append(botao)
        botoes.append(linha_botoes)

# Configurando a raiz
root = Tk()
root.title("Menu de Jogos")

# Definindo o tamanho padrão da janela principal
largura_principal = 300
altura_principal = 350

# Centralizando a janela principal
centralizar_janela(root, largura_principal, altura_principal)

# Frame para o menu
frame_menu = Frame(root)
frame_menu.pack(pady=10)

# Label do menu
msg = Label(frame_menu, text="Menu", font=("Verdana", 38, "bold"))
msg.pack(pady=10)

# Botão para abrir a janela do Sudoku
botao_sudoku = Button(frame_menu, text="Sudoku", width=15, command=sudoku_janela)
botao_sudoku.pack(pady=(25, 15))

# Botão para abrir a janela do Jogo da Velha
botao_jogo_da_velha = Button(frame_menu, text="Jogo da Velha", width=15, command=jogo_da_velha_janela)
botao_jogo_da_velha.pack(pady=15)

# Botão para sair
botao_sair = Button(root, text="Sair", font=("Verdana", 10), width=5, command=root.quit)
botao_sair.pack(side=BOTTOM, pady=(0, 25))

# Iniciando o loop principal da aplicação
root.mainloop()
