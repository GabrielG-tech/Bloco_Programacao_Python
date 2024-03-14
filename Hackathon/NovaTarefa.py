import tkinter as tk
from util import definirTamanhoTela

add_janela = None

def abrir_nova_janela():
    global add_janela

    if add_janela is not None and add_janela.winfo_exists():
        add_janela.lift()
    else:
        nova_janela = tk.Toplevel()
        nova_janela.title("Nova Tarefa")
        label = tk.Label(nova_janela, text="Nova Tarefa")
        label.pack(expand=True, side="top", pady=8, padx=15)
        definirTamanhoTela()
    
