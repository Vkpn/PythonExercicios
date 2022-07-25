mat = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        mat[x].append(int(input(f'Digite um valor para [{x},{y}]: ')))
print('=-=' * 10)
for p in range(0, len(mat)):
    print(mat[p])
