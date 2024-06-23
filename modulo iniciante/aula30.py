"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
#forma de 'mudar' o valor de uma str
string = 'Felipe'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)

#capitalize() retorna a str com a primeira letra maiúscula
print(string.capitalize())