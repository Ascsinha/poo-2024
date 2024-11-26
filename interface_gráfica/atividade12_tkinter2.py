from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Calculadora")
janela.geometry("400x300+200+200")

rotulo1 = Label(janela, text="Valor 1: ")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2: ")
rotulo2.grid(row=1, column=0)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo3 = Label(janela, text="SOMA = ")
rotulo3.grid(row=3, column=0)

campo3 = Entry(janela, state="")
campo3.grid(row=3, column=1)

rotulo4 = Label(janela, text="SUBTRAÇÃO = ")
rotulo4.grid(row=5, column=0)

campo4 = Entry(janela, state="disabled")
campo4.grid(row=5, column=1)

rotulo5 = Label(janela, text="MULTIPLICAÇÃO = ")
rotulo5.grid(row=8, column=0)

campo5 = Entry(janela, state="disabled")
campo5.grid(row=8, column=1)

rotulo6 = Label(janela, text="DIVISÃO = ")
rotulo6.grid(row=11, column=0)

campo6 = Entry(janela, state="disabled")
campo6.grid(row=11, column=1)

def somar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    soma = v1 + v2
    campo3.delete(0, END)
    campo3.insert(0, soma)
    msg = f"A soma é igual a {subtracao}."
    messagebox.showinfo(message=msg)

botao = Button(janela)
botao.grid(row=2, column=1)
botao["width"] = 15
botao["text"] = "Somar"
botao["command"] = somar

def subtrair():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    subtracao = v1 - v2
    campo4.delete(0, END)
    campo4.insert(0, subtracao)
    msg = f"A soma é igual a {subtracao}."
    messagebox.showinfo(message=msg)

botao = Button(janela)
botao.grid(row=6, column=1)
botao["width"] = 15
botao["text"] = "Subtrair"
botao["command"] = subtrair

def multiplicar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    multiplicacao = v1 * v2
    campo5.delete(0, END)
    campo5.insert(0, multiplicacao)
    msg = f"A soma é igual a {multiplicacao}."
    messagebox.showinfo(message=msg)

botao = Button(janela)
botao.grid(row=9, column=1)
botao["width"] = 15
botao["text"] = "Multiplicar"
botao["command"] = multiplicar
         
def dividir():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    divisao = v1/v2
    campo5.delete(0, END)
    campo5.insert(0, divisao)
    msg = f"A soma é igual a {divisao}."
    messagebox.showinfo(message=msg)

botao = Button(janela)
botao.grid(row=12, column=1)
botao["width"] = 15
botao["text"] = "Dividir"
botao["command"] = dividir

janela.mainloop()

