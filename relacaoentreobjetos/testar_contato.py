from data import Data
from contato import Contato

nome = input("Digite o nome do contato: ")
telefone = int(input("Digite o telefone do contato: "))
dia = int(input("Digite o dia do nascimento do contato: "))
mes = int(input("Digite o mes do nascimento do contato: "))
ano = int(input("Digite o ano do nascimento do contato: "))

data_nascimento = Data(dia, mes, ano)
contato = Contato(nome, telefone, data_nascimento)
contato.exibirContato()