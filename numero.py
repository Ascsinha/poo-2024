class Numero:

    def __init__(self, num):
        self.num = num
    
    def sucessor(self):
        valor = self.num + 1
        print(f'O sucessor de {self.num} é {valor}.')

    def antecessor(self):
        ant = self.num - 1
        print(f'O sucessor de {self.num} é {ant}.')

    def dobro(self):
        dob = self.num * 2
        print(f'O dobro de {self.num} é {dob}.')

    def triplo(self):
        trip = self.num * 3
        print(f'O triplo de {self.num} é {trip}.')

    def metade(self):
        met = self.num / 2
        print(f'A metade de {self.num} é {met}.')

num1 = Numero(2)
num1.sucessor()
num1.antecessor()
num1.dobro()
num1.triplo()
num1.metade()

num2 = Numero(8)
num2.sucessor()
num2.antecessor()
num2.dobro()
num2.triplo()
num2.metade()
