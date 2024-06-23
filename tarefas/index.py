def valida_cpf(cpf):

    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:
        return False

    if all(digito == cpf[0] for digito in cpf):
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    dv1 = 11 - resto if resto > 1 else 0
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    dv2 = 11 - resto if resto > 1 else 0

    return cpf[9] == str(dv1) and cpf[10] == str(dv2)


while True:
    opcao1_respondida = False

    print("Escolha uma opção:")
    print("[1] Incluir Conveniado")
    print("[2] Consultar Tipo de Apólice")
    print("[3] Consultar Dados do Conveniado")
    print("[4] Calcular Valor da Mensalidade")

    opcao1 = int(input("Digite sua opção: "))

    if opcao1 == 1:
        
        nome = input("Nome: ")
        cpf = input("CPF: ")
        
        if not valida_cpf(cpf):
            print("CPF inválido")
            exit()
        else:
            print('CPF valido')
        endereco = input("Endereço: ")
        valor_mensalidade = float(input("Valor da mensalidade: "))
        num_dependentes = int(input("Número de dependentes: "))
        opcao1_respondida = True

    elif opcao1 == 2:
        if not opcao1_respondida:
            print("É necessário responder à opção 1 primeiro.")
            continue
        else:
            tipo_apolice = input("Tipo de apólice (Bronze, Prata ou Ouro): ")
            if tipo_apolice == "Bronze":
                valor_beneficiario = 600.00
            elif tipo_apolice == "Prata":
                valor_beneficiario = 800.00
            elif tipo_apolice == "Ouro":
                valor_beneficiario = 950.00
            else:
                print("Tipo de apólice inválido")

    elif opcao1 == 3:
        if not opcao1_respondida:
            print("É necessário responder à opção 1 primeiro.")
            continue
        else:
            print("Dados do conveniado:")
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Endereço: {endereco}")
            print(f"Valor da mensalidade: {valor_mensalidade}")
            print(f"Número de dependentes: {num_dependentes}")
        

    elif opcao1 == 4:
        if not opcao1_respondida:
            print("É necessário responder à opção 1 primeiro.")
            continue
        else:
            num_pessoas = int(input("Número de pessoas que usarão o convênio: "))
            valor_mensalidade = valor_beneficiario * num_pessoas
            print(f"Valor da mensalidade: {valor_mensalidade}")

    else:
        print("Opção inválida")
