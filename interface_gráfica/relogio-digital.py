from tkinter import *
import tkinter
from datetime import datetime

import pyglet 
pyglet.font.add_file("interface_gráfica\fontes\digital-7.ttf")

#Cores

#Decimal: 0123456789
#Binário: 01
#Hexadecimal: 0123456789ABCDEF

cor1 = "#3d3d3d" #Preta
cor2 = "#fafcff" #Branco
cor3 = "#21c25c" #Verde
cor4 = "#e50914" #Vermelho
cor5 = "#dedcdc" #Cinza
cor6 = "#3080f0" #Azul

fundo = cor1
cor = cor2

janela = Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(width = FALSE, height = FALSE)
janela.configure(bg = cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.strftime("%d")
    mes = tempo.strftime("%B") #B maiúsculo = Janeiro... b min = "Jan"
    ano = tempo.strftime("%Y")
    l1.config(text = hora)
    l1.after(200, relogio)
    l2.config(text = dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, font=("digital-7 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, font=("digital-7 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()



janela.mainloop()

