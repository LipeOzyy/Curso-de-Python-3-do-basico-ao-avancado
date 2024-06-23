"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
nome = input('Qual seu nome?: ')
pergunta_forca = input(f'olá {nome}, vamos jogar o jogo da forca?: ')

while True:
    if pergunta_forca == 'Sim' or pergunta_forca == 'sim' or pergunta_forca == 'SIM':
            pergunta_dica = input('Você quer uma dica?: ')
            if pergunta_dica == 'sim' or pergunta_dica == 'Sim':
                print('Dica!! "cheiro bom"')
            elif pergunta_dica == 'não' or pergunta_dica == 'Não':
                print('Uauu, então vamos lá')
            else:
                print('Responda com sim ou não')
                break
            while True:
                letra_digitada = input('Digite uma letra: ')
                numero_tentativas += 1

                if len(letra_digitada) > 1:
                    print('Digite apenas uma letra')
                    continue
            
                if letra_digitada in palavra_secreta:
                    letras_acertadas += letra_digitada

                palavra_formada = ''
                for letra_secreta in palavra_secreta:
                    if letra_secreta in letras_acertadas:
                        palavra_formada += letra_secreta
                    else:
                        palavra_formada += '*'
                
                print('Palavra formada: ', palavra_formada)

                if palavra_formada == palavra_secreta:
                    os.system('cls')
                    print('PARA A BENS !!! VOCÊ GANHOU')
                    print('A palavra secreta era', palavra_formada)
                    print('Numero de tentativas:', numero_tentativas)
                    letras_acertadas = ''
                    numero_tentativas = 0
    elif pergunta_forca == 'Não' or pergunta_forca == 'NÃO' or pergunta_forca == 'não':
            print('Tudo bem, talvez mais tarde...')
    else:
        print('Responda apenas com "sim" ou "não"')
        break