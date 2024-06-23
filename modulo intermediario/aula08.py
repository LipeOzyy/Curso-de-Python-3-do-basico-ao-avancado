def mult (a, b):
    return a * b
Numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

resultado = mult(Numero1, numero2)

print(resultado)

#________________________________________________#

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

result = mult(10, 2, 3, 4, 5)
print(result)
#________________________________________________#

def why(num):
    if num % 2 == 0:
        return 'par'
    return "impar"


num = int(input("Digite um numero: "))
result = why(num)
print(result)




