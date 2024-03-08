import tkinter as tk

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Janela")
    label = tk.Label(nova_janela, text="Esta é uma nova janela!")
    label.pack()

root = tk.Tk()
root.title("Janela Principal")

botao = tk.Button(root, text="Abrir Nova Janela", command=abrir_nova_janela)
botao.pack()

root.mainloop()
