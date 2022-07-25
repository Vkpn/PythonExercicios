val = float(input('Qual o valor do produto? R$'))
pag = str(input('Dinheiro, cartão, 2x ou mais? ')).lower()

if pag == 'mais':
    parc = int(input('Qual a quantidade de parcelas? '))

vdin = val - (val * 10 / 100)
vcar = val - (val * 5 / 100)
v2x = val / 2
v3x = val + (val * 20 / 100)

if pag == 'dinheiro':
    print('O valor total ficou de R$ {:.2f} por R$ {:.2f} com desconto de 10%.'.format(val, vdin))
elif pag == 'cartão' or pag == 'cartao':
    print('O valor total ficou de R$ {:.2f} por R$ {:.2f} com desconto de 5%.'.format(val, vcar))
elif pag == '2x':
    print('O valor total ficou de R$ {:.2f} dividido em 2 parcelas iguais de R$ {:.2f}.'.format(val, v2x))
elif pag == 'mais':
    print('O valor total ficou de R$ {:.2f} dividido em {} parcelas de R$ {:.2f} considerando o juros de 20% no valor total.'.format(v3x, parc, (v3x / parc)))



