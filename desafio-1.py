menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

==>"""

saldo = 0
limite_diario_por_deposito = 3000
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_POR_DIA = 3

while True:

    opcao = input(menu)

    # DEPOSITOS

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        excedeu_limite_deposito = valor >= limite_diario_por_deposito

        if excedeu_limite_deposito:
            print("Operação falho! Valor do deposito acima do permitido por dia, que é de R$: 3.000,00")

        elif valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # SAQUES

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_por_saque

        excedeu_sques = numero_saques >= LIMITE_SAQUES_POR_DIA

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_sques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    # EXTRATOS

    elif opcao == "3":
        print("\n======================== EXTRATO ========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=========================================================")

    # FINALIZAR OPERAÇÕES

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")