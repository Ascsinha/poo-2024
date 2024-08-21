class Conta_bancaria:

    def __init__(self, titular, cpf, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo = saldo

    def mostrar_conta(self):
        return f"Nome do titular: {self.__titular}\n, CPF: {self.__cpf}\n, Saldo bancário: {self.__saldo}"

    def depositar(self, deposito):
        x = self.__saldo + deposito
        return f"Com o depósito de R${deposito}, seu saldo aumentou para R${x}"

    def sacar(self, saque):
        if saque >= self.__saldo:
            x2 = self.__saldo - saque
            return f"Com o saque de R${saque} realizado, seu saldo atual é de R${x2}"
        else:
            print("Valor inválido!")

    def verificar_saldo(self):
        return f"Seu saldo atual é de R${self.__saldo}"

    
