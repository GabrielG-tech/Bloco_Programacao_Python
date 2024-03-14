from tkinter import *
from NovaTarefa import abrir_nova_janela

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

add = Button(header, text="Adicionar tarefa", bg="#6aa84f", bd=0, pady=8, padx=15, fg="white", font=("Arial", 10, "bold"), command=abrir_nova_janela)
add.pack(side=LEFT)

definirTamanhoTela(root)

# for tarefa in listaTarefas:
#     print(tarefa)
#     tarefa = Frame(window)
#     tarefa.pack(fill=X, expand=True, padx=10, pady=10)
#     nome = Label(tarefa, text=f"{tarefa.get('nome')}")
#     nome.pack(side=LEFT)
#     tarefa.pack()


root.mainloop()
