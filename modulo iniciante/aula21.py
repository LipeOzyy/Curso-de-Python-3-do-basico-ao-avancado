# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

#---------------------------------------------------------------------------
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair') 
#---------------------------------------------------------------------------

#Avaliação de curto circuito
# print(True or False or 0) 
# print(False or False or 'abc' or False or True)
# print(False or False or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)

