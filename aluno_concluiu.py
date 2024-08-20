from aluno2 import *

class Aluno_Concluiu(Aluno):

    def __init__(self, matricula, nome, curso, data_conclusao, emitiu_certificado):
        super().__init__(matricula, nome, curso)
        self.__data_conclusao = data_conclusao
        self.__emitiu_certificado = emitiu_certificado
    
    def getData_conclusao(self):
        return(self.__data_conclusao)

    def getEmitiu_certificado(self):
        return(self.__emitiu_certificado)

    def setData_conclusao(self, data_conclusao):
        self.__data_conclusao = data_conclusao

    def setEmitiu_certificado(self, emitiu_certificado):
        self.__emitiu_certificado = True


aluno1 = Aluno_Concluiu("20201041110008", "Dudu", "Informática", "2023", False)
print(aluno1.getNome(), aluno1.getMatricula(), aluno1.getCurso(), aluno1.getData_conclusao(), aluno1.getEmitiu_certificado())
