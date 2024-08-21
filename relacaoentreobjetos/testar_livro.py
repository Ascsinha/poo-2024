from capitulo import Capitulo
from livro2 import Livro

numero = int(input("Digite o número do capítulo: "))
titulo = input("Digite o título do capítulo: ")
texto = input("Digite o texto do capítulo: ")

capitulo1 = Capitulo(numero, titulo, texto)
capitulo1.exibirCapitulo()

capitulo1 = Capitulo(1, "Introdução a Orientação a Objetos", "X....")
capitulo2 = Capitulo(2, "Encapsulamento", "Y....")
capitulo3 = Capitulo(3, "Herança", "Z....")

livro_de_poo = Livro("Orientação a Objetos em Python", "Alba Lopes", 2024)
livro_de_poo.adicionarCapitulo(capitulo1)
livro_de_poo.adicionarCapitulo(capitulo2)
livro_de_poo.adicionarCapitulo(capitulo3)