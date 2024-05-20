from tkinter import *

fontePadrao = "Verdana"

def centralizar_janela(janela, largura, altura):
    # Obtendo as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calculando a posição para centralizar a janela
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Definindo a geometria da janela
    janela.geometry('{}x{}+{}+{}'.format(largura, altura, pos_x, pos_y))

def sudoku_janela():
    nova_janela = Toplevel(root)
    centralizar_janela(nova_janela, largura_principal, altura_principal)
    nova_janela.title("Sudoku")
    
    # Criando um frame para os widgets
    frame = Frame(nova_janela, width=200, height=200, bg="green")
    frame.pack()

    # Entry
    quadradoEntry = Entry(frame, width=5, font=fontePadrao)
    quadradoEntry.pack(padx=5, pady=5)

def jogo_da_velha_janela():
    nova_janela = Toplevel(root)
    centralizar_janela(nova_janela, largura_principal, altura_principal)
    nova_janela.title("Jogo da Velha")
    
    # Criando um frame para os widgets
    frame = Frame(nova_janela, bg="gray")
    frame.pack(pady=10)

    # Função para lidar com o clique em um botão do tabuleiro
    def clicar_botao(linha, coluna, tabuleiro):
        # Verificar se a célula está vazia
        if tabuleiro[linha][coluna] == " ":
            # Atualizar o texto do botão com a jogada do jogador atual
            botoes[linha][coluna].config(text=jogador_atual)
            # Trocar para o próximo jogador
            trocar_jogador()
            # Verificar se alguém ganhou ou se deu velha
            verificar_resultado()

    # Função para trocar para o próximo jogador
    def trocar_jogador():
        global jogador_atual
        jogador_atual = "X" if jogador_atual == "O" else "O"

    # Função para verificar se alguém ganhou ou se deu velha
    def verificar_resultado():
        # Implemente a lógica de verificação de vitória ou empate aqui
        pass

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
root.title("Sudoku Demo")

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

# Botão para abrir uma nova janela
botao_novo_jogo = Button(frame_menu, text="Sudoku", width=15, command=sudoku_janela)
botao_novo_jogo.pack(pady=(25,15))

botao_novo_jogo = Button(frame_menu, text="Jogo da Velha", width=15, command=jogo_da_velha_janela)
botao_novo_jogo.pack(pady=15)

# Botão para sair
botao_sair = Button(root, text="Sair", font=("Verdana", 10), width=5, command=root.quit)
botao_sair.pack(side=BOTTOM, pady=(0, 25))

# Iniciando o loop principal da aplicação
root.mainloop()
