from tkinter import *
from Utils import definirTamanhoTela
# pip install tkcalendar
from tkcalendar import DateEntry
from locale import setlocale, LC_ALL

# Define o locale para português do Brasil
setlocale(LC_ALL, 'pt_BR')

add_janela = None

def abrir_nova_janela(editar=False):
    """
    Cria uma nova janela com campos para adicionar o nome, descrição e data de uma tarefa.
    A data é selecionada usando o widget DateEntry do tkcalendar, que retorna um objeto "datetime.date".
    """
    global add_janela

    if add_janela is not None and add_janela.winfo_exists():
        add_janela.lift()
    else:
        nova_janela = Toplevel()

        window = Frame(add_janela)
        window.pack(fill=BOTH, expand=True)

        header = Frame(window)
        header.pack(fill=X, expand=True, side=TOP, padx=10, pady=10)
        
        # Nome da tarefa
        label_nome = Label(nova_janela, text="Nome da Tarefa")
        label_nome.pack(padx=5, pady=(50, 5))
        campo_nome = Entry(nova_janela, width=30)
        campo_nome.pack(padx=5, pady=5)
        
        # Descrição da tarefa
        label_descricao = Label(nova_janela, text="Descrição da Tarefa")
        label_descricao.pack(padx=10, pady=5)
        campo_descricao = Entry(nova_janela, width=30)
        campo_descricao.pack(padx=5, pady=5)
        
        # Data da tarefa
        label_data = Label(nova_janela, text="Data da Tarefa")
        label_data.pack(padx=10, pady=5)
        campo_data = DateEntry(nova_janela, width=28, background='darkblue', foreground='white', borderwidth=2, locale='pt_BR', date_pattern='dd/mm/yyyy')
        campo_data.pack(padx=5, pady=5)

        # Botão
        btnAddTarefa = Button(nova_janela, text="Enviar", bg="#6aa84f", bd=0, pady=8, padx=15, fg="white", font=("Arial", 10, "bold"))
        btnAddTarefa.pack(pady=10)
        
        definirTamanhoTela(nova_janela, 300, 400)
