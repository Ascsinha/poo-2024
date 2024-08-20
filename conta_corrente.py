from conta_b import Conta_bancaria

class Conta_corrente(Conta_bancaria):

    def __init__(self, titular, cpf, saldo, numerocc):
        super().__init__(titular, cpf, saldo)
        self.__numerocc = numerocc

    def mostrarcc(self):
        super().mostrar_conta()
        return f"Número da conta corrente: {self.__numerocc}."

    