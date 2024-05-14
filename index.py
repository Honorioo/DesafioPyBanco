menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    

    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")

        valor = float(input("Qual valor vc quer depositar? "))
        
        if valor > 0:
            saldo += valor
            extrato += "Depósito: R$ {valor:.2f}\n"
            print(f'Seu saldo agora é {saldo}')
        else:
            print("O valor digitado foi negativo!")

    elif opcao == 's':
        print("Saque")

        valor = float(input("Qual valor vc quer sacar? "))

        if valor > saldo:
            print(f"""Você exedeu o seu saldo
                    Saldo : {saldo}
                  """)
        elif valor > limite: 
            print("Esse valor excede o seu limite diario de saque que é R$500,00")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"""Você exedeu o numero de saques diarios
                    Limite de saque : {numero_saques}
                  """)
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += 'Saque: R$ {valor:.2f}\n'


    elif opcao == 'e':
        print("Extrato")

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == 'q':
        break
    
    else:
        print("Operação falhou! O valor informado é inválido.")

     