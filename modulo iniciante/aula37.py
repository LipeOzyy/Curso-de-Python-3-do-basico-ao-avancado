frase = 'O Python é uma linguagem de programção ' \
    'multiparadigma. Python foi criado por Guido van Rossum'

i = 0
qnt_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qnt_apareceu_mais_vezes < quantas_vezes_letra_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = quantas_vezes_letra_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
    
    i += 1
    
    print(f'A letra que apareceu mais vezes foi '
          f'{letra_que_apareceu_mais_vezes} que apareceu '
          f'{qnt_apareceu_mais_vezes}x')
   