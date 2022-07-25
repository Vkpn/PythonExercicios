from math import factorial
num = factorial(int(input('Digite o numero para saber seu fatorial: ')))
print(num)

print('==' * 30)

numero = int(input('Digite um numero para saber seu fatorial: '))
numerofinal = numero
anterior = numero - 1
contador = numero
while contador > 2:
    numero = (numero * anterior)
    anterior -= 1
    contador -= 1
print('O fatorial de {} é {}'.format(numerofinal, numero))
