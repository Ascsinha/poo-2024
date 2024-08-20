class Cofrinho:

    def __init__(self, valor, meta):
        self.valor = valor
        self.meta = meta

    def adicionar(self, quantia):
       self.valor = self.valor + quantia  

    def falta(self):
        x = self.meta - self.valor 
        print(f'Falta R$ {x} para os R$ {self.meta} da sua meta.')

    def falta(self):
        if self.valor == self.meta:
            print('PARABÉNS, você chegou na sua meta!')
        elif self.valor > self.meta:
            print('Você ultrapassou a sua meta!')
            self.excesso = self.valor - self.meta
        else:
            x = self.meta - self.valor
            print(f'Falta {x} para os {self.meta} da sua meta.')

meta_rennan = Cofrinho(7000, 20000)
meta_rennan.adicionar(400)
meta_rennan.falta()
meta_rennan.adicionar(350)
meta_rennan.falta()   
meta_rennan.adicionar(15000)
meta_rennan.falta()                