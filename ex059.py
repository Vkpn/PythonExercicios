n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
continuar = 's'.upper()
while continuar == 'S':
    print('==' * 30)
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR VALOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    print('==' * 30)
    menu = int(input('Qual operação deseja realizar: '))
    if menu == 1:
        print('==' * 30)
        print('A soma dos valores é {}'.format(n1 + n2))
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        print('==' * 30)
    elif menu == 2:
        print('==' * 30)
        print('A multiplicaçao desses valores é {}'. format(n1 * n2))
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        print('==' * 30)
    elif menu == 3:
        print('==' * 30)
        if n1 > n2:
            print('O maior numero é {}'.format(n1))
        elif n1 < n2:
            print('O maior numero é {}'.format(n2))
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif menu == 5:
        continuar = 'N'
print('Programa finalizado')
