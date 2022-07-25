p = float(input('Qual o preço do produto? R$ '))
print('O valor do produto é R${}, porém na liquidação com o desconto de 5% o valor final fica R$ {:.2f} .'.format(p, (p/100)*95))