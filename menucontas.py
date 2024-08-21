from conta_b import Conta_bancaria
from conta_corrente import Conta_corrente
from conta_poupança import Conta_poupanca

print("===== Bem-vindo ao Banco Nacional =====")
print("O que deseja?")
print("1) Criar minha conta")
print("2) Acessar minha conta")
print("3) Sair")

Conta_corrente = []
Conta_poupanca = []

escolha = int(input("Digite sua escolha: "))
while escolha != 3:

    if escolha == 1:
        titular = input("Informe o nome do titular da conta: ")
        cpf = input("Informe o CPF do titular: ")
        tipo = int(input("Informe o tipo de conta: 1) Conta corrente  2) Conta poupança: "))
        
        if tipo == 1:
            numerocc = input("Informe o número da sua conta corrente: ")
            deposito = int(input("Deseja depositar um valor em sua conta? 1) Sim  2) Não: "))

            if deposito == 1:
                saldo = 0
                deposito = float(input("Insira o valor de depósito: R$ "))
                valor1 = saldo + deposito
                mov = Conta_bancaria.depositar(deposito, valor1)
                saq = int(input("Deseja sacar algum valor? 1) Sim  2) Não: "))

                if saq == 1:
                    valor_saque = float(input("Insira o valor do saque: R$ "))
                    saque = Conta_bancaria(valor_saque)
                    print(Conta_bancaria.sacar())
                    print(Conta_bancaria.verificar_saldo())
                    print("Obrigado por escolher o Banco Nacional!")

                elif saq == 2:
                    print("Obrigado por escolher o Banco Nacional!")

                else: 
                    print("Opção inválida!")

            elif deposito == 2:
                print("Obrigado por escolher o Banco Nacional!")

            else:
                print("Opção inválida!")
            
        elif tipo == 2:
            deposito = int(input("Deseja depositar um valor em sua conta? 1) Sim  2) Não: "))

            if deposito == 1:
                deposito = float(input("Insira o valor de depósito: R$ "))
                saldo = 0
                print(Conta_bancaria.depositar(deposito, saldo))
                sac = int(input("Deseja sacar algum valor? 1) Sim  2) Não: "))

                if sac == 1:
                    valor_saque = float(input("Insira o valor do saque: R$ "))
                    saque = Conta_bancaria(valor_saque)
                    print(Conta_bancaria.sacar())
                    print(Conta_bancaria.verificar_saldo())
                    print("Obrigado por escolher o Banco Nacional!")

                elif sac == 2:
                    print("Obrigado por escolher o Banco Nacional!")

                else: 
                    print("Opção inválida!")

            elif deposito == 2:
                print("Obrigado por escolher o Banco Nacional!")

            else:
                print("Opção inválida!")
        
    elif escolha == 2:
        titular = input("Informe o nome do titular da conta: ")
        cpf = input("Informe o CPF do titular: ")
        acesso = int(input("Deseja acessar as informações de que conta? 1) Conta corrente  2) Conta poupança: "))

        if acesso == 1:
            print(Conta_bancaria.verificar_saldo())
            mov_bancaria = int(input("Deseja realizar alguma movimentação em sua conta? 1) Saque  2) Depósito  3) Ver minhas informações  4) SAIR "))

            if mov_bancaria == 1:
                valor_saque = float(input("Insira o valor do saque: R$ "))
                saque = Conta_bancaria(valor_saque)
                print(Conta_bancaria.sacar())
                print(Conta_bancaria.verificar_saldo())
                print("Obrigado por escolher o Banco Nacional!")
                
            elif mov_bancaria == 2:
                deposito = float(input("Insira o valor de depósito: R$ "))
                valor1 = saldo + deposito
                mov = Conta_bancaria.depositar(deposito, valor1)
                saq = int(input("Deseja sacar algum valor? 1) Sim  2) Não: "))

            elif mov_bancaria == 3:
                informacoes = Conta_bancaria(titular, cpf, saldo, numerocc)
                print(Conta_corrente.mostrarcc())

            elif mov_bancaria == 4:
                print("Agradecemos a sua confiança!")

            else:
                print("Opção inválida!")
            
        elif acesso == 2:
            print(Conta_bancaria.verificar_saldo())
            print(f"e o rendimento da sua conta poupança é de: R${Conta_poupanca.ver_rendimento()}. Sendo assim, o valor atual do seu saldo é de: R${Conta_poupanca.render()}")
            mov_bancaria = int(input("Deseja realizar alguma movimentação em sua conta? 1) Saque  2) Depósito  3) Ver minhas informações  4) SAIR "))

            if mov_bancaria == 1:
                valor_saque = float(input("Insira o valor do saque: R$ "))
                saque = Conta_bancaria(valor_saque)
                print(Conta_bancaria.sacar())
                print(Conta_bancaria.verificar_saldo())
                print("Obrigado por escolher o Banco Nacional!")
                
            elif mov_bancaria == 2:
                deposito = float(input("Insira o valor de depósito: R$ "))
                valor1 = saldo + deposito
                mov = Conta_bancaria.depositar(deposito, valor1)
                saq = int(input("Deseja sacar algum valor? 1) Sim  2) Não: "))

            elif mov_bancaria == 3:
                informacoes = Conta_bancaria(titular, cpf, saldo)
                print(Conta_bancaria.mostrar_conta())
                print(Conta_poupanca.ver_rendimento(), Conta_poupanca.render())

            else:
                print("Opção inválida!")

    else:
        print("Agradecemos a sua confiança!")