"""
Faça uma lista de comprar com listas
O usuario deve ter a posibilidade de inserir, 
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de
indices inexistentes na lista.
"""
#MEU CODIGO FICOU ASSIM, MEIO BUNDA

# lista_user = []

# while True:

#     opicao_usuario = input('Selecione uma opção \n'
#             '[I]nserir [E]cluir [L]istar [S]air: ')
    
#     if opicao_usuario == "I" or opicao_usuario == "i":
#         add = input('Oque você deseja inserir na lista: ')
#         lista_user.append(add)
#         if add == lista_user:
#             print('Esse item já está na lista')
#         else:
#             print(f'o intem {add} foi inserido na lista')
#             continue

#     elif opicao_usuario == "E" or opicao_usuario == "e":
#         remover = input('Oque você deseja excluir da lista: ')
#         if remover in lista_user:
#             lista_user.remove(remover)
#         else: 
#             print('esse item não está na lista')

#     elif opicao_usuario == "L" or opicao_usuario == "l":
#         print(lista_user)
    
#     elif opicao_usuario == "S" or opicao_usuario == "s":
#         break


#     else: 
#         print('essa opção não existe!')
#         continue

#CODIGO DO PROFESSOR 
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')