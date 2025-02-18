from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Ana era uma garota que morava em uma região fria. Um dia, sua mãe lhe contou um relato sobre pessoas que foram infectadas pelo Cordyceps no sul, um fungo que causava mutações genéticas, consequentemente mudanças físicas e comportamentais. Isso causou curiosidade na menina. Cética com o relato, Ana, acompanhada do seu irmão mais novo, pegou sua mochila e partiu em direção ao desconhecido. \n\n

        Por um longo período de tempo, Ana andou até finalmente chegar no sul. Ela, junto com o irmão, chegou em uma cidade deserta. Observando a cidade percebeu-se que nela não havia habitantes. 
        '''
        self.__opcoes = ["Mesmo assim, Ana decidiu ficar e explorar.", "Ana viu que seria perigoso ficar e explorar, e decidiu voltar com seu irmão para o vilarejo."]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()
        
class Parte2(Fase):
    def __init__(self):
        self.__descricao ='''Você encontra uma recepção, mas está
        trancada. 
        '''
        self.__opcoes = ["entrar pelo duto de ar ", "seguir para a ala cirúrgica."]


    def executar(self):
        print("\nParte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte4()
        else:
            return Parte5()
        
class Parte3(Fase):
    def __init__(self):
        self.__descricao ='''Você encontra um caminho que leva
        a ala psiquiátrica.
        '''
        self.__opcoes = ["Porta 1", "Porta 2"]

    def executar(self):
        print("\nParte 3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()
        
class Parte4(Fase):
    
    def executar(self):
        print('''Você tenta entrar, mas não consegue
              Você tenta entrar pelo duto de ar
              mas não aguenta seu peso. Você cai e morre!
              ''')
        
        return None

class Parte5(Fase):
    
    def executar(self):
        print('''Você segue para a ala de cirurgia. Lá 
              você encontra o remédio na estante.
              ''')
        
        return None

class Parte6(Fase):
    
    def executar(self):
        print('''Você se depara com diversos experimentos
              com pessoas. lá você cai em uma armadilha
              e morre!
              ''')
        
        return None
    
class Parte7(Fase):
    
    def executar(self):
        print('''Você encontra o remédio na gaveta da mesa.
              ''')
        
        return None