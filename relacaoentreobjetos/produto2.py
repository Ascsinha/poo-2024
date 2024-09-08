class Produto:

    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def setNome(self):
        self.__nome = nome

    def setPreco(self):
        self.__preco = preco

    def setQuantidade(self):
        self.__quantidade = quantidade

    def getNome(self):
        return self.nome

    def getPreco(self):
        return self.__preco

    def getQuantidade_estoque(self):
        return self.__quantidade

    def exibirProduto(self):
        print(f"Nome: {self.__nome}\n Preço: {self.__preco}\n Quantidade em estoque: {self.__quantidade}")