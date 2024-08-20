class Cofrinho:

    def __init__(self, valor, meta):
        self.__valor = valor #private
        self.meta = meta #public

# get ---> recuperar o valor de um atributo privado
# set ---> alterar o valor de um atributo privado

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        if valor >= 0:
            self.__valor = valor
        
