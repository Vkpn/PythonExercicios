listagem = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
max = len(listagem)
item = 0
pre = 1
print('=' * 32)
print('{:^30}'.format('Listagem de preços'.upper()))
print('=' * 32)

while True:
    if pre <= max:
        print('{:.<21}'.format(listagem[item]), 'R$', '{:>7.2f}'.format(listagem[pre]))
        item += 2
        pre += 2
    elif pre >= max:
        break
print('=' * 32)
