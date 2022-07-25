num = input('Escreva um numero inteiro entre 0 e 9999: ').rjust(4, '0')
print('O numero digitado foi: {}'.format(num))
print('Temos {} unidade(s).'.format(num[3]))
print('Temos {} dezena(s).'.format(num[2]))
print('Temos {} centena(s).'.format(num[1]))
print('Temos {} milhar(es).'.format(num[0]))














