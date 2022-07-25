from random import randint
from time import sleep

jogo = {}
for j in range(1, 5):
    jogador = 'Jogador ' + str(j)
    jogo[jogador] = randint(1, 6)

print('=' * 30)
print(f'{"jogo de dados".upper():^30}')
print('=' * 30)

for j, n in jogo.items():
    sleep(0.8)
    print(f'O {j} tirou {n}')

print('=' * 30)
print(f'{"resultado".upper():^30}')
print('=' * 30)

pos = 1

for j in sorted(jogo, key=jogo.get, reverse=True):
    sleep(0.8)
    print(f'{pos}° lugar: {j} com {jogo[j]}')
    pos += 1
