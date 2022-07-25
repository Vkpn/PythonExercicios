from random import randint

num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(num)
print(f'Os números ordenados ficam: {sorted(num)}')
print(f'O maior número foi: {max(num)}')
print(f'O menor número foi: {sorted(num)[0]}')

