from conta_b import Conta_bancaria

class Conta_poupanca(Conta_bancaria):

    def __init__(self, titular, cpf, saldo, rendimento):
        super().__init__(titular, cpf, saldo)
        self.__rendimento = rendimento

    def ver_rendimento(self):
        self.__rendimento = 0.005
        return self.__rendimento

    def render(self):
        return self.saldo * self.__rendimento
