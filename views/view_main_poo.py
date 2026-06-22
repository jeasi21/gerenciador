import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from dados.dataBase import *


class Main:
    def __init__(self):
        self.janela = tk.Tk()

        largura = 1280
        altura = 720

        lagura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x=int((lagura_tela / 2) - (largura / 2))
        y=int((altura_tela / 2) - (altura / 2))

        self.janela.geometry(f'{largura}x{altura}+{x}+{y}')
        self.janela.title('Sistema de controle')
        self.janela.iconbitmap(default='./imgs/user0.ico')
        #janela.geometry('1024x680')
        #self.janela.resizable(False,False)

        self.lnome = tk.Label(self.janela, text="Nome", font=("Helvetica", 16))
        self.lnome.place(relx=0.17, rely=0.06)
        self.eNome = tk.Entry(self.janela,font=("Helvetica", 14))
        self.eNome.place(relx=0.17, rely=0.096, relwidth=0.6)

        self.ltel = tk.Label(self.janela, text="Telefone",font=("Helvetica", 16))
        self.ltel.place(relx=0.17, rely=0.14)
        self.eTel = tk.Entry(self.janela,font=("Helvetica", 14))
        self.eTel.place(relx=0.17, rely=0.176, relwidth=0.6)

        self.lemail = tk.Label(self.janela, text="Email",font=("Helvetica", 16))
        self.lemail.place(relx=0.17, rely=0.22, )
        self.eEmail = tk.Entry(self.janela,font=("Helvetica", 14))
        self.eEmail.place(relx=0.17, rely=0.256, relwidth=0.6)

        self.lplano = tk.Label(self.janela, text="Plano",font=("Helvetica", 16))
        self.lplano.place(relx=0.17, rely=0.33)
        self.ePlano = tk.Entry(self.janela, font=("Helvetica", 14))
        self.ePlano.place(relx=0.17, rely=0.366,relwidth=0.095)

        self.lvencimento = tk.Label(self.janela, text="Vencimento",font=("Helvetica", 16))
        self.lvencimento.place(relx=0.374, rely=0.33)
        self.eVencimento = tk.Entry(self.janela, font=("Helvetica", 14))
        self.eVencimento.place(relx=0.375, rely=0.366,relwidth=0.095)

        #buscar:::
        self.lpesquisar = tk.Label(self.janela, text="Buscar por nome",font=("Helvetica", 16))
        self.lpesquisar.place(relx=0.594, rely=0.33)
        self.ePesquisar = tk.Entry(self.janela, font=("Helvetica", 14),)
        self.ePesquisar.bind("<KeyRelease>", self.buscar_usuario)
        self.ePesquisar.place(relx=0.595, rely=0.366,relwidth=0.18)


        #btns:::
        self.btnSalvar = tk.Button(self.janela, text="Salvar",font=("Helvetica", 14), command=self.salvar_usuario)
        self.btnSalvar.configure(bg='green', fg='white')
        self.btnSalvar.place(relx=0.17, rely=0.42, relwidth=0.08)

        self.btnAtualizar = tk.Button(self.janela, text="Atualizar",font=("Helvetica", 14), command=self.atualizar_usuario)
        self.btnAtualizar.configure(bg='blue', fg='white')
        self.btnAtualizar.place(relx=0.44, rely=0.42, relwidth=0.08)

        self.btnDeletar = tk.Button(self.janela, text="Deletar",font=("Helvetica", 14),command=self.deletar_usuario)
        self.btnDeletar.configure(bg='red', fg='white')
        self.btnDeletar.place(relx=0.69, rely=0.42, relwidth=0.08)


        #tabela:::
        self.tabela = ttk.Treeview(self.janela, columns=('id', 'nome', 'tel', 'email', 'plano', 'vencimento'), show='headings')
        self.tabela.heading('id', text='Id')
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('tel', text='Telefone')
        self.tabela.heading('email', text='E-Mail')
        self.tabela.heading('plano', text='Plano')
        self.tabela.heading('vencimento', text='Vencimento')

        self.tabela.column("id", width=50)
        self.tabela.column("tel", width=120)
        self.tabela.column("plano", width=60)
        self.tabela.column("vencimento", width=60)
        self.tabela.bind("<Double-1>", self.carregar_dados)

        self.scroll = tk.Scrollbar(self.janela, orient='vertical', command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=self.scroll.set)

        self.scroll.place(relx=0.964,rely=0.51,width=20,relheight=0.375)
        self.tabela.place(relx=0.015, rely=0.5, relwidth=0.97, relheight=0.4)

        self.tabelaReload()

        self.lAutor = tk.Label(self.janela, text="Created by Jeasi21", font=("Helvetica", 9))
        self.lAutor.place(relx=0.49, rely=0.95)
      


    def tabelaReload(self):
        dados = exibir_clientes()
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for dado in dados:
            self.tabela.insert("", tk.END, values= dado)
    
        #self.janela.after(5000, self.tabelaReload)


    def salvar_usuario(self):
        nome = self.eNome.get()
        tel = self.eTel.get()
        email = self.eEmail.get()
        plano = self.ePlano.get()
        vencimento = self.eVencimento.get()
    
        if all([nome,tel,email,plano,vencimento]):
            salvar_cliente(nome, tel, email, plano, vencimento)
            messagebox.showinfo('INFO', 'Dados salvos com sucesso!')
            self.tabelaReload()
        else:
            messagebox.showinfo('INFO','Preencha todos os dados do cliente!')

        self.eNome.delete(0,END)
        self.eTel.delete(0,END)
        self.eEmail.delete(0,END)
        self.ePlano.delete(0,END)
        self.eVencimento.delete(0,END)



    def deletar_usuario(self):
        id_usuario = self.tabela.item(self.tabela.selection()[0], 'values')[0]
        usuario_nome = self.tabela.item(self.tabela.selection()[0], 'values')[1]

        if id_usuario != "":
            resp = messagebox.askokcancel('Confirmação', f"Deletar Usuario {usuario_nome}?")
            if resp:
                excluir_cliente(id_usuario)
                messagebox.showinfo('INFO', 'Usuário deletado com sucesso!')
                self.tabelaReload()
        
        '''   
        item= self.tabela.selection()
        if item:
            valores = self.tabela.item(item[0], 'values')
            id_usuario = valores[0]
        
            excluir_cliente(id_usuario)
        '''
     
       
    def carregar_dados(self,event):
        item = self.tabela.selection()
        if item:
            valores = self.tabela.item(item[0], 'values')
            self.eNome.delete(0,END)
            self.eNome.insert(0, valores[1])

            self.eTel.delete(0,END)
            self.eTel.insert(0, valores[2])

            self.eEmail.delete(0,END)
            self.eEmail.insert(0, valores[3])

            self.ePlano.delete(0,END)
            self.ePlano.insert(0, valores[4])

            self.eVencimento.delete(0,END)
            self.eVencimento.insert(0, valores[5])

            #messagebox.showinfo('Dado selecionado', valores)

    def atualizar_usuario(self):
        id_usuario = self.tabela.item(self.tabela.selection()[0], 'values')[0]
        nome = self.eNome.get()
        tel = self.eTel.get()
        email = self.eEmail.get()
        plano = self.ePlano.get()
        vencimento = self.eVencimento.get()
    
        if all([id_usuario,nome,tel,email,plano,vencimento]):
            atualizar_cliente(id_usuario, nome, tel, email, plano, vencimento)
            messagebox.showinfo('INFO', 'Dados atualizados com sucesso!')
            self.tabelaReload()
        else:
            messagebox.showinfo('INFO','Selecione um usuario!')

        self.eNome.delete(0,END)
        self.eTel.delete(0,END)
        self.eEmail.delete(0,END)
        self.ePlano.delete(0,END)
        self.eVencimento.delete(0,END)
    
    def buscar_usuario(self, event):
        nome_pesquisado = self.ePesquisar.get()

        dados = buscar_cliente(nome_pesquisado)
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        
        for dado in dados:
            self.tabela.insert("",'end', values=dado)

        
        
if __name__ == '__main__':
    app = Main()
    app.janela.mainloop()