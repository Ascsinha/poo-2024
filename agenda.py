from contato import Contato

class Agenda:

    def __init__(self):
        self.__contato = []

    def inserir_contato(self, contato):
        self.__contato.append(contato)
    
    def buscar_contato(self, nome):
        for contato in self.__contatos:
            if contato.get_nome().lower() == nome.lower():
                return contato
        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.__contatos.remove(contato)
            return True
        return False

    def listar_contatos(self):
        if not self.__contatos:
            print("Agenda vazia.")
        else:
            for contato in self.__contatos:
                contato.exibirContato()


