from tkinter import *

janela = Tk()

rotulo = Label(janela, text="Olá, Mundo!")
rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial", "16", "bold")
rotulo["fg"] = "blue"

rotulo2 = Label(janela, text="Tudo bem?")
rotulo2.grid(row=1, column=0)
rotulo2["font"] = ("Arial", "14", "bold")
rotulo2["fg"] = "gold"

rotulo3 = Label(janela, text="Linguagem de Programação Python")
rotulo3.grid(row=2, column=0)
rotulo3["font"] = ("Arial", "12", "bold")
rotulo3["width"] = 50

botao_sair = Button(janela)
botao_sair.grid(row=4, column=0, pady=10)
botao_sair["bg"] = "blue"
botao_sair["fg"] = "white"
botao_sair["text"] = "Sair"
botao_sair["width"] = 10
botao_sair["command"] = quit

imagem = PhotoImage(file="D:/Users/20231041110004/Desktop/poo-2024/poo-2024/interface_gráfica/Imagem/python.png")
rotulo2 = Label(janela, image= imagem)
rotulo2.grid(row=3, column=0, pady=10)
rotulo2["width"] = 150
rotulo2["height"] = 150

janela.mainloop()