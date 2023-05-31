# importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# ======== Criar nossa janela ==================

jan = Tk()
# Nome do seu painel
jan.title("Esperança Nordeste - Painel de Acesso")
# Tamanho do seu painel
jan.geometry("600x300")
# Cor de fundo do seu painel
jan.configure(background="white")
# Se seu painel vai ser responsivo 
jan.resizable(width=False, height=False)
# adicionar um icone 
jan.iconbitmap(default="icons/LogoIcon.ico")

# ========= Carregando Imagens =====================
logo = PhotoImage(file="icons/logo.png")

# ========= widgets / das janelas ==================
# parte da esquerda
LeftFrame = Frame(jan, width=200, height=300, bg="green", relief="raised")
LeftFrame.pack(side=LEFT)
# parte da direita 
RightFrame = Frame(jan, width=395, height=300, bg="green", relief="raised")
RightFrame.pack(side=RIGHT)
# parte da imagem
logoLabel = Label(LeftFrame, image=logo, bg="green")
logoLabel.place(x=50, y=100)

# parte de login
UserLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="green", fg="white")
UserLabel.place(x=5, y=100)
# entrada de dados do login
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=100, y=112)

# parte da senha 
PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="green", fg="white")
PassLabel.place(x=5, y=140)
# entrada de dados da senha
PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=100, y=152)


# inserir os botões de acesso
LoginButton = ttk.Button(RightFrame, text="Acesso", width=30)
LoginButton.place(x=100, y=200)


def Registrar():
    # removendo wigets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000) 
    # inserindo wigets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="green", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=40)
    NomeEntry.place(x=100, y=20)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="green", fg="white")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=42)
    EmailEntry.place(x=88, y=64)

    def RegisterToDataBaser():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Nome == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Erro no Registro", message="Nao Deixe Nenhum Campo Vazio. Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Usuarios(Nome, Email, Usuario, Senha) VALUES(?, ?, ?, ?)
            """,(Nome, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Informação de Registro", message="Conta Criada com Sucesso!")

    Register = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBaser)
    Register.place(x=100, y=200)

    def BackToLogin():
        # Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        # Trazendo de volta os Widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125) 


    Back = ttk.Button(RightFrame, text="Voltar", width=23, command=BackToLogin)
    Back.place(x=120, y=235)


# inserir os botões de registro
RegisterButton = ttk.Button(RightFrame, text="Registro", width=23, command=Registrar)
RegisterButton.place(x=120, y=235)


jan.mainloop()