ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
contador = 10
while contador > 0:
    print(ter, end=' ')
    ter += raz
    contador -= 1
