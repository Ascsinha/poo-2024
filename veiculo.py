class Veiculo:
    
    def __init__ (self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

carro1 = Veiculo('Gol', 'Volkswagen', 2015)
print (f'Marca do carro 1: {carro1.marca}.')

carro1.modelo = 'Voyage'
print (f'Novo modelo do carro 1: {carro1.modelo}.')

carro2 = Veiculo('Ford Ka', 'Ford', 2018)
print (f'Modelo do carro 2: {carro2.modelo}.')