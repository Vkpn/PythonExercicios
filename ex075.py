val = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')), int(input('Digite o 3° valor: ')), int(input('Digite o 4° valor: ')))

print(f'Voce digitou os valores: {val}')
print(f'o valor 9 apareceu {val.count(9)} vezes.')
if 3 in val:
    print(f'O valor 3 apareceu na {val.index(3) + 1} posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares digitados foram: ', end='')
for c in range(0, 4):
    if val[c] % 2 == 0:
        print(val[c], end=' ')

