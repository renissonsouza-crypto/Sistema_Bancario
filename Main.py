import csv 
from datetime import datetime 

import matplotlib.pyplot as plt

saldo = 100
extrato = []
historico_saldo = [saldo]  # guarda o saldo após cada movimentação, para plotar depois
ARQUIVO_CSV = "extrato_movimentacao.csv"


def salvar_no_csv(tipo, valor):
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), tipo, f"{valor:.2f}", f"{saldo:.2f}"]
        )


def exibir_banco():
    print("\n===== CAIXA ELETRONICO =====")
    print("1- Consultar Saldo")
    print("2- Depositar Dinheiro")
    print("3- Sacar Dinheiro")
    print("4- Ver Extrato")
    print("5- Movimentações")
    print("6- Sair")


def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")


def depositar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser depositado R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        historico_saldo.append(saldo)  # adiciona o novo saldo na lista do gráfico
        salvar_no_csv("Depósito", valor)
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nValor inválido.")


def sacar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser sacado R$ "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        historico_saldo.append(saldo)  # adiciona o novo saldo na lista do gráfico
        salvar_no_csv("Saque", valor)
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nSaldo insuficiente ou valor inválido.")


def ver_extrato():
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")


def ver_movimentacoes():
    plt.plot(historico_saldo, marker="o")  # desenha a lista de saldos, um ponto por movimentação
    plt.title("Evolução do Saldo")
    plt.ylabel("Saldo (R$)")
    plt.show()


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
            ver_extrato()
        elif opcao == "5":
            ver_movimentacoes()
        elif opcao == "6":
            print("\nSaindo do sistema. Obrigado por utilizar o Caixa Eletrônico.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
