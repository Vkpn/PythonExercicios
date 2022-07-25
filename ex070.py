print('**' * 20)
baner = 'Lojão do Victor'
print('{:^40}'.format(baner))
print('**' * 20)
tot = 0
prod1000 = 0
prodbar = ''
valprodbar = 0
cont = 0
while True:
    prod = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o valor do produto: R$ '))
    continuar = ' '
    tot += preco
    if cont == 0:
        prodbar = prod
        valprodbar = preco
        cont += 1
    if valprodbar > preco:
        prodbar = prod
        valprodbar = preco
    if preco > 1000:
        prod1000 += 1
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'O total gasto na compra foi de R${tot:.2f}')
print(f'Nessa compra {prod1000} produtos custam mais de R$ 1000.00')
print(f'O {prodbar} é o produto mais barato, custando R${valprodbar:.2f}')
