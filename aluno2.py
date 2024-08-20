from mailbox import NotEmptyError


class Aluno:

    def __init__(self, matricula, nome, curso):
        self.__matricula = matricula
        self.__nome = nome
        self.__curso = curso

    def getMatricula(self):
        return self.__matricula

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setNome(self, nome):
        self.__nome = nome 

    def setCurso(self, curso):
        self.__curso = curso
