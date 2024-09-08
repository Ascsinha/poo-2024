from autor import Autor
from livro3 import Livro
from biblioteca import Biblioteca

print("====== Bem-vindo à Biblioteca IFZN ======")
print("Que ação deseja realizar?")
print("1) Adicionar um novo livro ao acervo")
print("2) Buscar um livro no acervo")
print("3) Remover um livro")
print("4) Listar todos os livros disponíveis")
print("5) Sair")
print("=========================================")

biblioteca = Biblioteca()

escolha = int(input("Escolha uma das opções acima: "))
while True:

    if escolha == 1:
        titulo = input("Insira o nome do novo livro: ")
        biblioteca.adicionarLivro()

    elif escolha == 2:
        titulo = input("Digite o título do livro desejado: ")
        livro = biblioteca.buscarLivro()
        if livro:
            livro.exibirLivro()
        else:
            print("Livro não encontrado.")

    elif escolha == 3:
        titulo = input("Digite o título do livro que deseja remover: ")
        if biblioteca.removerLivro(titulo):
            print("Livro removido com sucesso.")
        else:
            print("Livro não encontrado.")

    elif escolha == 4:
        biblioteca.listarLivros()

    elif escolha == 5:
        print("Sessão finalizada!")
        break

    else:
        print("Escolha indisponível. Por favor, tente novamente.")







