print('Digite vários valores para saber a soma entre todos eles:')
print('Para parar digite o valor 999.')
print('==' * 30)
cont = 0
tot = 0
num = 0
while num != 999:
    tot += num
    cont += 1
    num = int(input('Digite o {}° valor: '.format(cont)))
print('\033[31mPrograma finalizado.\033[m')
print('==' * 30)
print('A soma total dos {} valores digitados é: {}'. format(cont - 1, tot))
