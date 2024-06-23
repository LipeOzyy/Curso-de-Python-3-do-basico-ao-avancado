while True:
    print("Escolha uma opção:")
    print("[1] Incluir Conveniado")
    print("[2] Consultar Tipo de Apólice")
    print("[3] Consultar Dados do Conveniado")
    print("[4] Calcular Valor da Mensalidade")

    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço completo: ")
        numero_dependentes = int(input("Digite o número total de dependentes: "))
        print("Digite o tipo de apólice:")
        print("[1] Bronze - R$600.00 por beneficiário")
        print("[2] Prata - R$800.00 por beneficiário")
        print("[3] Ouro - R$950.00 por beneficiário")
        tipo_apoliche = input("Escolha o tipo de apólice (1, 2, 3): ")
        if tipo_apoliche == '1':
            valor_mensalidade = 600.00 * (numero_dependentes + 1)
            tipo_apoliche = "Bronze"
        elif tipo_apoliche == '2':
            valor_mensalidade = 800.00 * (numero_dependentes + 1)
            tipo_apoliche = "Prata"
        elif tipo_apoliche == '3':
            valor_mensalidade = 950.00 * (numero_dependentes + 1)
            tipo_apoliche = "Ouro"
        print(f"Conveniado {nome} cadastrado com sucesso! Tipo de apólice: {tipo_apoliche}, Valor da mensalidade: R${valor_mensalidade:.2f}")

    elif opcao == '2':
        print("Você escolheu consultar o tipo de apólice. (Exemplo: Ouro)")

    elif opcao == '3':
        print("Você escolheu consultar os dados do conveniado. (Exemplo: Nome: João, CPF: 123.456.789-00)")

    elif opcao == '4':
        print("Você escolheu calcular o valor da mensalidade. (Exemplo: R$ 2850.00)")

    else:
        print("Opção inválida!")