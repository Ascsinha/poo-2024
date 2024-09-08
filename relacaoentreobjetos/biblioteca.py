from livro3 import Livro

class Biblioteca(Livro):

    def __init__(self):
        self.__livro = [Livro]

    def adicionarLivro(self, livro):
        self.__livro.append(livro)

    def buscarLivro(self, livro, titulo):
        for livro in self.__livro:
            if livro.getTitulo().lower() == titulo.lower():
                return titulo
        return None

    def removerLivro(self, livro):
        livro = self.buscarLivro(livro)
        if livro:
            self.__livro.remove(livro)
            return True
        return False

    def listarLivros(self):
        if not self.__livro:
            print("Biblioteca vazia.")
        else:
            for livro in self.__livro:
                livro.exibirLivro()

