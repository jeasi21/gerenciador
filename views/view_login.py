import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from dados import data_adms


janela_login = tk.Tk()

largura = 380
altura = 420

lagura_tela = janela_login.winfo_screenwidth()
altura_tela = janela_login.winfo_screenheight()
x=int((lagura_tela / 2) - (largura / 2))
y=int((altura_tela / 2) - (altura / 2))

janela_login.geometry(f'{largura}x{altura}+{x}+{y}')
janela_login.resizable(False, False)
#janela_login.iconbitmap(default='./imgs/user0.ico')
janela_login.title("Login")


login_txt = tk.Label(janela_login,text='Login', font=('helvetica', 26))
login_txt.place(relx=0.38, rely=0.05, relheight=0.25, relwidth=0.25)

userlb = tk.Label(janela_login, text='Usuario', font=('helvetica', 12))
userlb.place(relx=0.25, rely=0.3)

user = tk.Entry(janela_login, font=('helvetica', 14))
user.place(relx=0.25, rely=0.36, relwidth=0.55)

user_passlb = tk.Label(janela_login, text='Senha', font=('helvetica', 12))
user_passlb.place(relx=0.25, rely=0.46)

user_pass = tk.Entry(janela_login, font=('helvetica', 14), show="*")
user_pass.place(relx=0.25, rely=0.52, relwidth=0.55)

def logar_admin():
    usr = user.get()
    psw = user_pass.get()
    data_adms.logar_adms(usr, psw)
    user.delete(0,END)
    user_pass.delete(0,END)
    janela_login.destroy()
 



def sair():
    janela_login.destroy()


btn_login = tk.Button(janela_login, text="Entrar",font=('helvetica', 14), command=logar_admin)
btn_login.configure(bg='green', fg='white')
btn_login.place(relx=0.25, rely=0.61)

btn_logout = tk.Button(janela_login, text="Sair",font=('helvetica', 14), command=sair)
btn_logout.configure(bg='red', fg='white')
btn_logout.place(relx=0.66, rely=0.61)



janela_login.mainloop()