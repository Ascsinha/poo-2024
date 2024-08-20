from aluno2 import *

class Aluno_cursando(Aluno):

    def __init__(self, matricula, nome, curso, ano_atual, ano_concluir):
        super().__init__(matricula, nome, curso)
        self.__ano_atual = ano_atual
        self.__ano_concluir = ano_concluir
    
    def getAno_atual(self):
        return(self.__ano_atual)

    def getAno_concluir(self):
        return(self.__ano_concluir)

    def setAno_atual(self, ano_atual):
        self.__ano_atual = ano_atual
        print(f"Ano vigente: {self.__ano_atual}.")

    def setAno_concluir(self, ano_concluir):
        self.__ano_concluir = ano_concluir
        print(f"Ano de conclusão: {self.__ano_concluir}.")

aluno_cursando1 = Aluno_cursando("20231041110004", "Acsa", "Informática", 2024, 2027)
print(aluno_cursando1.getNome(), aluno_cursando1.getMatricula(), aluno_cursando1.getCurso())
aluno_cursando1.setAno_atual(2024)
aluno_cursando1.setAno_concluir(2027)