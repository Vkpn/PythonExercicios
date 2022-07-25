num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
       'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
       'Dezoito', 'Dezenove', 'Vinte')

continuar = 'S'
while continuar not in 'Nn':
    while continuar in 'Ss':
        numero = int(input('Digite um numero de 0 a 20: '))
        if 0 > numero or numero > 20:
            print('Fora do alcance. ')
        else:
            print(f'Você digitou o numero {num[numero]}')
        break
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('Fim')
