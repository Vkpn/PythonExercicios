mat = [[], [], []]
valp = 0
valt = 0
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x},{y}]: '))
        if num % 2 == 0:
            valp += num
        mat[x].append(num)
print('=-=' * 10)
for p in mat:
    print(p)
print('=-=' * 10)
print(f'A soma dos valores pares é {valp}.')
for c in range(0, 3):
    valt += (mat[c][2])
print(f'A soma dos valores da terceira coluna é {valt}.')
mais = sorted(mat[1])
print(f'O maior valor da segunda linha é {mais[2]}.')
