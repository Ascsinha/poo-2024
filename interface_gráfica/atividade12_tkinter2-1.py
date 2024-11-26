from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Boas-vindas")
janela.geometry("300x200+100+100")

rotulo = Label(janela, text="Qual é o seu nome? ")
rotulo.grid(row=0, column=0)

campo = Entry(janela, show="*")
campo.grid(row=1, column=0)

def boasvindas(): 
    nome = campo.get()
    msg = f"Acesso permitido. Seja bem-vindo(a), {nome}!"
    messagebox.showinfo(message=msg)

botao = Button(janela)
botao.grid(row=2, column=0)
botao["text"] = "Entrar"
botao["command"] = boasvindas

janela.mainloop()