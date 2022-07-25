s = float(input('Qual o valor do salário atual? R$ '))
print('Salário atual: {:.2f}\nValor do aumento: {:.2f}\nValor final após o aumento: {:.2f}'.format(s, (s/100)*15, s+(s/100)*15))
