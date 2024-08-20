class Animal:
    def __init__ (self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

animal1 = Animal('Rex', 'Cachorro', 3)
print (f'Nome do animal: {animal1.nome}.')

animal1.idade = 4
print (f'Nova idade do animal 1: {animal1.idade}.')

animal2 = Animal('Mimosa', 'Gato', 5)
print (f'Idade do animal 2: {animal2.idade}.')

