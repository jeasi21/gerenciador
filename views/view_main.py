import tkinter as tk
from tkinter import messagebox, ttk
from dados.dataBase import *

janela = tk.Tk()

largura = 1024
altura = 680

lagura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x=int((lagura_tela / 2) - (largura / 2))
y=int((altura_tela / 2) - (altura / 2))

janela.geometry(f'{largura}x{altura}+{x}+{y}')
#janela.geometry('1024x680')
janela.title('Sistema de controle')
janela.resizable(False,False)

lnome = tk.Label(janela, text="Nome", font=("Helvetica", 16))
lnome.place(relx=0.17, rely=0.06)
eNome = tk.Entry(janela,font=("Helvetica", 14))
eNome.place(relx=0.17, rely=0.1, relwidth=0.6)

ltel = tk.Label(janela, text="Telefone",font=("Helvetica", 16))
ltel.place(relx=0.17, rely=0.14)
eTel = tk.Entry(janela,font=("Helvetica", 14))
eTel.place(relx=0.17, rely=0.18, relwidth=0.6)

lemail = tk.Label(janela, text="Email",font=("Helvetica", 16))
lemail.place(relx=0.17, rely=0.22, )
eEmail = tk.Entry(janela,font=("Helvetica", 14))
eEmail.place(relx=0.17, rely=0.27, relwidth=0.6)

def tabelaReload():
    for item in tabela.get_children():
        tabela.delete(item)

    for dado in exibir_dados():
        tabela.insert("", tk.END, values= dado)
    
    janela.after(2000, tabelaReload)


def salvar():
    nome = eNome.get()
    tel = eTel.get()
    email = eEmail.get()
  
    messagebox.showinfo('teste', chamarNome(nome))


def atualizar():
    #teste pegando dados
    item = tabela.selection()
    if item:
        valores = tabela.item(item[0], 'values')

        messagebox.showinfo('Dado selecionado', valores)


def deletar():
    pass

def exibir_dados():
    pass

btnSalvar = tk.Button(janela, text="Salvar",font=("Helvetica", 14), command=salvar)
btnSalvar.configure(bg='green', fg='white')
btnSalvar.place(relx=0.17, rely=0.42, relwidth=0.08)

btnAtualizar = tk.Button(janela, text="Atualizar",font=("Helvetica", 14), command=atualizar)
btnAtualizar.configure(bg='blue', fg='white')
btnAtualizar.place(relx=0.44, rely=0.42, relwidth=0.08)

btnDeletar = tk.Button(janela, text="Deletar",font=("Helvetica", 14),command=deletar)
btnDeletar.configure(bg='red', fg='white')
btnDeletar.place(relx=0.69, rely=0.42, relwidth=0.08)

tabela = ttk.Treeview(janela, columns=('Id', 'Nome', 'Telefone', 'E-mail'), show='headings')
for col in ('Id', 'Nome', 'Telefone', 'E-mail'):
    tabela.heading(col, text=col)

scroll = tk.Scrollbar(janela, orient='vertical', command=tabela.yview)
tabela.configure(yscrollcommand=scroll.set)

scroll.place(relx=0.859,rely=0.52,width=20,height=200)
tabela.place(relx=0.08, rely=0.5, relwidth=0.8)

direitos = tk.Label(janela, text="@Created By Jeasi21@", font=('Helvatica', 8))
direitos.place(relx=0.41, rely=0.97)


#nomes = ['maria', 'angela', 'gleice', 'gabriela']

#for i in nomes:
    #tabela.insert("",tk.END,values=i)


#tabelaReload()

janela.mainloop()