class Produto:
    
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

produto1 = Produto('Notebook', 3500.00, 10)
print (f'Preço do produto 1: R$ {produto1.preco}.')

produto1.preco = 3800.00
print (f'Novo preço do produto 1: R$ {produto1.preco}')

produto2 = Produto('Mouse', 50.00, 100)
print (f'Quantidade em estoque do produto 2: {produto2.quantidade}')
