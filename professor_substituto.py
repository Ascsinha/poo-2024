from professor import *

class Professor_Substituto(Professor):
    
    def __init__(self, nome, endereco, telefone, email, salario, tempo_contrato):
        super().__init__(nome, endereco, telefone, email, salario)
        self.tempo_contrato = tempo_contrato

    def mostrar_professor(self):
        print(self.get_nome, self.get_telefone, self.tempo_contrato)

professor1 = Professor_Substituto("Jhonatas", "Rua João da Silva", "4002-8922", "email@hotmail.com", "R$ 25000", "6 meses")
professor1.mostrar_professor()                                                                                                                              

    