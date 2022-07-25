from time import sleep
fra = str(input('Digite uma frase para saber se é um palíndromo: '))
fraed = fra.strip().upper().split()
frajun = ''.join(fraed)
print('Para saber se é um palíndromo, vamos primeiro retirar os espaços:')
sleep(2)
print(f'A palavra ficou: {frajun}')
sleep(2)
print('Agora vamos inverter a palavra:')
sleep(2)
print('A palavra invertida ficou: {}'.format(frajun[::-1]))
sleep(2)
print('Comparando com a palavra inicial temos: {} e {}'.format(frajun, frajun[::-1]))
sleep(2)
if frajun == frajun[::-1]:
    print('Podemo concluir que "{}" é um palíndromo!'.format(fra.upper()))
else:
    print('"{}" não é um palíndromo.'.format(fra.upper()))



