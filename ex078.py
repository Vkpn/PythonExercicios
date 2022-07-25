lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite o valor na posição {cont}: ')))
if lista.count(max(lista)) == 1:
    print(f'O maior valor digitado foi {max(lista)} que está na posição {lista.index(max(lista))}.', end=' ')
else:
    print(f'O maior valor digitado foi {max(lista)} que está nas posições', end=' ')
    for cmax, vmax in enumerate(lista):
        if max(lista) == vmax:
            print(cmax, end=' ')
if lista.count(min(lista)) == 1:
    print(f'\nO menor valor digitado foi {min(lista)} que está na posição {lista.index(min(lista))}.')
else:
    print(f'\nO menor valor digitado foi {min(lista)} que está nas posições', end=' ')
    for cmin, vmin in enumerate(lista):
        if min(lista) == vmin:
            print(cmin, end=' ')
