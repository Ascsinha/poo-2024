class Moto:

    def __init__(self, marca, modelo, cilindradas):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas

    def dados(self, modelo, cilindradas):
        print(f'A moto {self.modelo} possui {self.cilindradas} cilindradas.')

moto1 = Moto('Honda', 'Honda CB 500F', 500)
moto1.dados('Honda', 500)
print(f'Marca: {moto1.marca}. \nModelo: {moto1.modelo}. \nCilindradas: {moto1.cilindradas}.')

moto2 = Moto('Yamaha', 'Yamaha YZF-R6', 600)
moto2.dados('Yamaha YZF-R6', 600)
print(f'Marca: {moto2.marca}. \nModelo: {moto2.modelo}. \nCilindradas: {moto2.cilindradas}.')