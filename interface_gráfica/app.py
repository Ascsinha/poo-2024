from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #Preto
cor2 = "#feffff" #Branco
cor3 = "#38576b" #Azul
cor4 = "#eceff1" #Cinza
cor5 = "#ffab40" #Laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg = cor1)

frame_tela = Frame(janela, width = 235, height = 50, bg = cor3)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row = 1, column = 0)

todos_valores = ""

# Criando função 

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # resultado = eval("9/9")
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    # print(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

valor_texto = StringVar()
# Criando label

app_label = Label(frame_tela, textvariable = valor_texto, width = 16, height = 2, padx = 7, relief = FLAT, anchor = "e", justify = RIGHT, font = ("Ivy 18"), bg = cor3, fg = cor2)
app_label.place(x = 0, y = 0)

# Criando os botões

b1 = Button(frame_corpo, text = "C", command = lambda: limpar_tela(), width = 11, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b1.place(x = 0, y = 0)

b2 = Button(frame_corpo, text = "%", command = lambda: entrar_valores("%"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b2.place(x = 118, y = 0)

b3 = Button(frame_corpo, text = "/", command = lambda: entrar_valores("/"), width = 5, height = 2, bg = cor5, fg = cor2, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b3.place(x = 177, y = 0)


b4 = Button(frame_corpo, text = "7", command = lambda: entrar_valores("7"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b4.place(x = 0, y = 52)

b5 = Button(frame_corpo, text = "8", command = lambda: entrar_valores("8"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b5.place(x = 59, y = 52)

b6 = Button(frame_corpo, text = "9", command = lambda: entrar_valores("9"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b6.place(x = 118, y = 52)

b7 = Button(frame_corpo, text = "*", command = lambda: entrar_valores("*"), width = 5, height = 2, bg = cor5, fg = cor2, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b7.place(x = 177, y = 52)


b8 = Button(frame_corpo, text = "4", command = lambda: entrar_valores("4"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b8.place(x = 0, y = 104)

b9 = Button(frame_corpo, text = "5", command = lambda: entrar_valores("5"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b9.place(x = 59, y = 104)

b10 = Button(frame_corpo, text = "6", command = lambda: entrar_valores("6"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b10.place(x = 118, y = 104)

b11 = Button(frame_corpo, text = "-", command = lambda: entrar_valores("-"), width = 5, height = 2, bg = cor5, fg = cor2, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b11.place(x = 177, y = 104)


b12 = Button(frame_corpo, text = "1", command = lambda: entrar_valores("1"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b12.place(x = 0, y = 156)

b13 = Button(frame_corpo, text = "2", command = lambda: entrar_valores("2"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b13.place(x = 59, y = 156)

b14 = Button(frame_corpo, text = "3", command = lambda: entrar_valores("3"), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b14.place(x = 118, y = 156)

b15 = Button(frame_corpo, text = "+", command = lambda: entrar_valores("+"), width = 5, height = 2, bg = cor5, fg = cor2, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b15.place(x = 177, y = 156)


b16 = Button(frame_corpo, text = "0", command = lambda: entrar_valores("0"), width = 11, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b16.place(x = 0, y = 208)

b17 = Button(frame_corpo, text = ".", command = lambda: entrar_valores("."), width = 5, height = 2, bg = cor4, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b17.place(x = 118, y = 208)

b18 = Button(frame_corpo, text = "=", command = lambda: calcular(), width = 5, height = 2, bg = cor5, fg = cor2, font = ("Ivy 13 bold"), relief  = RAISED, overrelief = RIDGE)
b18.place(x = 177, y = 208)


janela.mainloop()