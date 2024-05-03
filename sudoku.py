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

def abrir_nova_janela():
    nova_janela = Toplevel(root)
    centralizar_janela(nova_janela, largura_principal, altura_principal)
    nova_janela.title("Sudoku I")
    
    # Criando um frame para os widgets
    frame = Frame(nova_janela)
    frame.pack(width=100, bg="green")

    # Label
    quadradoLabel = Label(frame, font=fontePadrao)
    quadradoLabel.pack(bg="black", padx=10, pady=10)

    # Entry
    quadradoEntry = Entry(frame, width=5, font=fontePadrao)
    quadradoEntry.pack(padx=5, pady=5)

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
botao_novo_jogo = Button(frame_menu, text="Novo jogo", width=15, command=abrir_nova_janela)
botao_novo_jogo.pack(pady=(25,15))

# Botão para sair
botao_sair = Button(root, text="Sair", font=("Verdana", 10), width=5, command=root.quit)
botao_sair.pack(side=BOTTOM, pady=(0, 25))

# Iniciando o loop principal da aplicação
root.mainloop()
