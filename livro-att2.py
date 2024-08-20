class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacoes(self, titulo, autor, paginas):
        print(f'O livro {self.titulo} do autor {self.autor} possui {self.paginas} páginas.')

livro1 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 323)
livro1.informacoes('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 323)
print(f'Título: {livro1.titulo}. \nAutor: {livro1.autor}. \nPáginas: {livro1.paginas}.')

livro2 = Livro('A Culpa é das Estrelas', 'John Green', 313)
livro2.informacoes('A Culpa é das Estrelas', 'John Green', 313)
print(f'Título: {livro2.titulo}. \nAutor: {livro2.autor}. \nPáginas: {livro2.paginas}.')

livro3 = Livro('A Máquina do Tempo', 'H. J. Wells', 112)
livro3.informacoes('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 112)
print(f'Título: {livro3.titulo}. \nAutor: {livro3.autor}. \nPáginas: {livro3.paginas}.')

