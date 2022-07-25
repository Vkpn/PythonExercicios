s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} números impares multiplos de 3 entre 1 e 500 é: {}'.format(cont, s))
