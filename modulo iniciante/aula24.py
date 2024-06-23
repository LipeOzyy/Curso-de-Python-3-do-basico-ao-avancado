"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Felipe'
preco = 100.000
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))