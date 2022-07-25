ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
contador = 10
while contador > 0:
    while contador > 0:
        print(ter, end=' ')
        ter += raz
        contador -= 1
    print('pausa...')
    print('=' * 40)
    contador = int(input('Gostaria de ver mais quantos termos? '))
print('Programa encerrado.')