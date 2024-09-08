from produto2 import Produto

class Venda(Produto):

    def __init__(self, dataVenda, total):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = total

    def getProdutos(self):
        return self.__produtos

    def getDataVenda(self):
        return self._dataVenda

    def getTotal(self):
        return self.__total

    def setProdutos(self):
        self.__produtos = produto

    def setDataVenda(self):
        self.__dataVenda = dataVenda

    def setTotal(self):
        self.__total = total

    def calcularTotal(self, calculo):
        self.__produtos = [preco]
        soma = 0
        for preco in produto:
            soma += preco
        return soma

