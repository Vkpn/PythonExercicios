n1 = int(input('Escreva um numero: '))
n2 = int(input('Escreva outro numero: '))
n3 = int(input('Escreva o ultimo numero: '))
numeros = [n1, n2, n3]
seq = sorted(numeros)
print('O maior numero entre eles é: {}'.format(seq[2]))
print('O menor numero entre eles é: {}'.format(seq[0]))

