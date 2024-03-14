from tkinter import *
from NovaTarefa import *
from Utils import *

listaTarefas = [{
    "id": 1,
    "nome": "Fazer compras",
    "descricao": "Fazer compras no mercado e comprar manteiga",
    "data": "2024-03-08",
    "concluido": False
}]

root = Tk()
root.title("Minhas tarefas")

window = Frame(root)
window.pack(fill=BOTH, expand=True)

header = Frame(window)
header.pack(fill=X, expand=True, side=TOP, padx=10, pady=10)

def abrir_janela_editar():
    abrir_nova_janela(True)

add = Button(header, text="Adicionar tarefa", bg="#6aa84f", bd=0, pady=8, padx=15, fg="white", font=("Arial", 10, "bold"), command=abrir_janela_editar)
add.pack(side=LEFT)

definirTamanhoTela(root)

for conteudo in listaTarefas:
    tarefa = Frame(window)
    tarefa.pack(fill=X, expand=True, padx=10, pady=10)
    nome = Label(tarefa, text=f"{conteudo.get('nome')}")
    nome.pack(side=LEFT)
    tarefa.pack()

root.mainloop()