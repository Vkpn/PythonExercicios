ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
for c in range(ter, (ter + (10 - 1) * raz) + raz, raz):
    print(c, end=' ')
print('FIM')
