from datetime import date

saldo = 100
extrato = []


def exibir_menu():
    print("\n===== CAIXA ELETRONICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("5 - Sair")


def consultar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")


def depositar():
    global saldo
    valor = float(input("Valor do deposito: R$ "))

    if valor <= 0:
        print("Valor invalido!")
        return

    saldo = saldo + valor
    registrar_movimentacao("deposito", valor)
    print(f"Deposito realizado! Saldo atual: R$ {saldo:.2f}")


def sacar():
    global saldo
    valor = float(input("Valor do saque: R$ "))

    if valor <= 0:
        print("Valor invalido!")
        return

    if valor > saldo:
        print("Saldo insuficiente!")
        return

    saldo = saldo - valor
    registrar_movimentacao("saque", valor)
    print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")


def ver_extrato():
    print("\n----- EXTRATO -----")

    if not extrato:
        print("Nenhuma movimentacao registrada ainda.")
        return

    for data_mov, tipo, valor, saldo_mov in extrato:
        print(f"{data_mov} | {tipo} | R$ {valor:.2f} | saldo: R$ {saldo_mov:.2f}")


def registrar_movimentacao(tipo, valor):
    data_hoje = date.today().strftime("%d/%m/%Y")
    extrato.append((data_hoje, tipo, valor, saldo))


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            ver_extrato()
        elif opcao == "5":
            print("Saindo... ate logo!")
            break
        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()
