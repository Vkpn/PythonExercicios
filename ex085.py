numeros = [[], []]
for n in range(0, 7):
    val = int(input(f'Digite o {n + 1}° valor: '))
    if val % 2 == 0:
        numeros[0].append(val)
    else:
        numeros[1].append(val)
print('-=-' * 15)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
