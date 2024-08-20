from pessoa import *

class Professor(Pessoa):

    def __init__(self, nome, endereco, telefone, email, salario):
        super().__init__(nome, endereco, telefone, email)
        self.salario = salario

    def get_salario(self):
        return(self.salario)

    def set_salario(self, salario):
        self.__salario = salario
        return("Sucesso")

professor1 = Professor('Mônica', 'Rua R', '9999-9999', 'monica@gmail.com', 'R$ 2600')
print(professor1.get_nome(), professor1.get_email(), professor1.get_salario())