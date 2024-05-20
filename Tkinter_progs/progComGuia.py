from tkinter import ttk
from tkinter import *

def centralizar_janela(janela, largura=300, altura=350):
    # Obtendo as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calculando a posição para centralizar a janela
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Definindo a geometria da janela
    janela.geometry('{}x{}+{}+{}'.format(largura, altura, pos_x, pos_y))


window = Tk()
window.title("Janela Foda")
centralizar_janela(window, 400, 450)

notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)

FrameA = Frame(notebook)
#
FrameA.pack(fill=BOTH, expand=True)

FrameB = Frame(notebook)
#
FrameB.pack(fill=BOTH, expand=True)

notebook.add(FrameA, text="Guia 1")
notebook.add(FrameB, text="Guia 2")

window.mainloop()
