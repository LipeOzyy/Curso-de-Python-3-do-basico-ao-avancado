 # texto_1 = 'Felipe tem 1,80 de altura e pesa 95kg, seu imc é:'
# print(texto_1, imc)
# # ou
# # print(nome, 'tem', altura, 'de altura', )
# print('pesa', peso, 'quilos e seu imc é')
# print(imc)


nome = 'Felipe'
altura = 1.80
peso = 95
imc = peso / (altura * altura) 


linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
print(linha_1)
print(linha_2)

# {:.numero f} isso define quantas casas ...
# decimais o numero pode ter
