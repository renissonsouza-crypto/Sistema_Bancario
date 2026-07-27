saldo = 100

def exibir_banco():
    print("\n===== CAIXA ELETRONICO =====")
    print("1- Consultar Saldo")
    print("2- Depositar Dinheiro")
    print("3- Sacar Dinheiro")
    print("4- Ver Extrato")
    print("5- Sair")

def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo}")

def depositar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser depositado R$ "))
    if valor > 0:
        saldo += valor
        print(f"\nDeposito de R$ {valor} realizado com sucesso.")
    else:
        print("\nValor inválido.")

def sacar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser sacado R$ "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print(f"\nSaque de R$ {valor} realizado com sucesso.")
    else:
        print("\nSaldo insuficiente ou valor inválido.")

def main():
    while True:
        exibir_banco()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar_dinheiro()
        elif opcao == "3":
            sacar_dinheiro()
        elif opcao == "4":
            print("\nExtrato não disponível no momento.")
        elif opcao == "5":
            print("\nSaindo do sistema. Obrigado por utilizar o Caixa Eletrônico.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

main()
