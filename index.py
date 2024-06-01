import textwrap

def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair

    => """

def depositar(saldo, valor, extrato):
    print("Depósito")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Seu saldo agora é R$ {saldo:.2f}')

    else:
        print("O valor digitado foi negativo!")

    return saldo, extrato

def saque(saldo, valor, extrato, numero_saques, limite, limite_saques):
    print("Saque")
    if valor > saldo:
        print(f"Você excedeu o seu saldo. Saldo: R$ {saldo:.2f}")

    elif valor > limite: 
        print("Esse valor excede o seu limite diário de saque que é R$ 500,00")

    elif numero_saques >= limite_saques:
        print(f"Você excedeu o número de saques diários. Limite de saques: {limite_saques}")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'
        print(f'Seu saldo agora é R$ {saldo:.2f}')

    else:
        print("O valor digitado foi negativo!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("Extrato")
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True: 

        opcao = input(menu())
        if opcao == 'd':
            valor = float(input("Qual valor você quer depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Qual valor você quer sacar? "))
            saldo, extrato, numero_saques = saque(saldo, valor, extrato, numero_saques, limite, LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print("Operação falhou! O valor informado é inválido.")

main()
