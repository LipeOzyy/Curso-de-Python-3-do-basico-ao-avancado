# Exercício - sistema de perguntas e respostas


questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for question in questions:
    print('Pergunta:', question['Pergunta'])
    print()

    opcoes = question['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    esc = input('opção: ')

    acertou = False
    esc_int = None
    qtd_opcoes = len(opcoes)

    if esc.isdigit():
        esc_int = int(esc)

    if esc_int is not None:
        if esc_int >= 0 and esc_int < qtd_opcoes:
            if opcoes[esc_int] == question['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(questions), 'perguntas.')



