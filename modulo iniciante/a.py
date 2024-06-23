nome = input('Qual seu nome: ')
print('Belo nome!')

idade = input('Qual sua idade: ')

if idade:
    idade_int = int(idade)
    ano_certo = input(f'{idade}?? Então você nasceu no ano de {idade_int - 2023},estou certo?: ')
    if ano_certo == 'Sim' or ano_certo =='sim' or ano_certo == 'SIM':
        print('Na mosca!!')
    elif ano_certo == 'Não' or ano_certo =='não' or ano_certo== 'NÃO':
        print('Quase, que pena!')
    else:
        print('Por favor digite apenas numeros!!')

job = input('Com oque você trabalha: ')
print('Trabalho legal!')

Pergunta_nome_letras = input('Quer saber quantas letras tem seu nome?: ') 

if Pergunta_nome_letras== 'Sim' or Pergunta_nome_letras== 'SIM' or\
    Pergunta_nome_letras == 'sim':
    print(f'seu nome tem {len(nome)} letras')
elif Pergunta_nome_letras == 'Não' or Pergunta_nome_letras =='não' or Pergunta_nome_letras== 'NÃO':
    print('Ok')

pergunta_dois = input('Quer saber mais algumas curiosidades sobre seu nome?:')
