n = int(input('Digite um numero para saber se esse numero é primo: '))
for c in range(2, n):
    if n % c == 0:
        print('{} não é um numero primo.'.format(n))
        break
    else:
        print('{} é um número primo.'.format(n))
        break
