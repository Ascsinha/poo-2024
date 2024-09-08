from autor import Autor

class Livro(Autor):
    
    def __init__(self, titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao

    def getAutor(self):
        return self.__autor

    def getTitulo(self):
        return self.__titulo

    def getAnoPublicacao(self):
        return self.__anoPublicacao

    def setAutor(self):
        print(f"Autor: {self.__autor.getNome()}")

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAnoPublicacao(self, anoPublicacao):
        self.__anoPublicacao = anoPublicacao

    def exibirLivro(self):
        print(f"Título: {self.__titulo}\n Autor: {self.__autor.exibirAutor()}\n Ano de publicação: {self.__anoPublicacao}")