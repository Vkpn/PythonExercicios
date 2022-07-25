import time
print('-' * 30)
print('Para aprovar seu emprestimo bancário, vamos precisar dos seguntes dados:')
print('-' * 30)
vcas = float(input('Qual o valor da casa que deseja comprar? R$'))
print('-' * 30)
sal = float(input('Qual o seu salário atual? R$'))
print('-' * 30)
temp = float(input('Em quantos anos deseja pagar o empréstimo? '))
print('-' * 30)
pmes = vcas / (temp * 12)

time.sleep(2)

if pmes > (sal * 30 / 100):
    print('\033[31mEmprestimo negado!\033[m R${:.2f} exede 30% do valor do seu salário.'.format(pmes))
else:
    print('O valor da prestação será de: \033[32mR${:.2f}'.format(pmes))
