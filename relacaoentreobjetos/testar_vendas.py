from produto2 import Produto
from venda import Venda

def adicionarProduto():
    self.__nome.append(nome)
    self.__preco.append(preco)
    self.__quantidade.append(quantidade)

def buscarProduto(self, produto):
    for produto in self.__produto:
        if produto.getNome().lower() == produto.lower():
            return titulo
    return None

def removerProduto(self, produto):
    produto = self.__produtos.buscarProduto(produto)
    if produto:
        self.__produto.remove(produto)
            return True
    return False

def exibirProdutos(self):
    print(f"Nome do produto: {nome}\n Preço: {preco}\n Unidades em estoque: {quantidade} unidades.")

def listarProdutos(self):
    if not self.__produtos:
        print("Estoque vazio.")   
    else:
        for produto in self.__produtos:
            produto.exibirProdutos()

print("====== Bem-vindo ao Supermercado Bom de Dev ======")
print("O que gostaria de fazerem nosso aplicativo? ")
print("1) Adicionar um novo produto a uma venda.")
print("2) Remover um produto da venda.")
print("3) Listar todos os produtos de uma determinada venda.")
print("4) Total a ser pago pela venda.")
print("5) Sair.")
print("==================================================")

venda = Venda()

escolha = int(input("Faça sua escolha: "))
while True:

    if escolha == 1:
        nome = input("Catalogue o nome do novo produto: ")
        preco = float(input("Dê um valor a ele: R$ "))
        quantidade = int(input("Quantas unidades estão estocadas? {} unidades."))
        produto.adicionarProduto()

    elif escolha == 2:
        nome = input("Digite o nome do produto que deseja remover do catálogo: ")
        if produto.removerProduto(nome, preco, quantidade):
            print("Produto removido com sucesso.")
        else: 
            print("Produto não encontrado.")

    elif escolha == 3:
        venda.listarProdutos()

    elif escolha == 4
        venda.calcularTotal()

    elif escolha == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")