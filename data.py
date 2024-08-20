class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = 1
        self.__mes = 1
        self.__ano = 0
        self.setDia(dia)
        self.setMes(mes)
        self.setAno(ano)

    def setDia(self, dia):
        if dia >= 1 and dia <= 31:
            self.__dia = dia

    def setMes(self, mes):
        if mes >= 1 and mes <= 12:
            self.__mes = mes

    def setAno(self, ano):
        if ano >= 0:
            self.__ano = ano

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def escreverData(self):
        print(f'{self.__dia}/{self.__mes}/{self.__ano}')