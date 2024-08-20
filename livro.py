from ast import AsyncFunctionDef


# Criando classe (Livro), função (def) e criando atributos (self.titulo, self.autor e self.ano).

class Livro:
    
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def info(self):
        print(f'O livro {self.titulo} foi escrito por {self.autor} em {self.ano}.')

# Criando métodos (livro1 = Livro()) e objetos (o resto).

livro1 = Livro('O nevoeiro', 'Stephen King', 1980)
print(f'O livro {livro1.titulo} foi escrito por {livro1.autor} em {livro1.ano}.')

livro1.ano = 1973
print(f'O livro {livro1.titulo} foi escrito por {livro1.autor} em {livro1.ano}.')

livro_angela = Livro('Coraline', 'Neil Gaiman', 2009)
print(f'O livro {livro_angela.titulo} foi escrito por {livro_angela.autor} em {livro_angela.ano}.')

livro1 = Livro('ABC', 'XYZ', 123)
livro1.info()
livro1.ano = 1973
livro1.info()

livro_angela = Livro('DEF', 'ABC', 456)
livro_angela.info()
