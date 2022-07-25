print('-~' * 20)
print('{:^40}'.format('Banco do Victor (BDV)').upper())
print('-~' * 20)
sacado = int(input('Qual o valor a ser sacado da conta? R$ '))
cinquenta = 0
vinte = 0
dez = 0
um = 0
while True:
    while sacado - 50 >= 0:
        cinquenta += 1
        sacado -= 50
    while sacado - 20 >= 0:
        vinte += 1
        sacado -= 20
    while sacado - 10 >= 0:
        dez += 1
        sacado -= 10
    while sacado - 1 >= 0:
        um += 1
        sacado -= 1
    break
if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de R$ 50')
if vinte != 0:
    print(f'Total de {vinte} cédulas de R$ 20')
if dez != 0:
    print(f'Total de {dez} cédulas de R$ 10')
if um != 0:
    print(f'Total de {um} cédulas de R$ 1')
print('-~' * 20)
print('Volte sempre ao BDV! Tenha um bom dia!')
