from random import randint
from time import sleep

print('-=-' * 10)
print(f'{"Joga na mega sena":^30}'.upper())
print('-=-' * 10)

apostas = []
jogos = []
njog = int(input('Quantos jogos você quer que eu sorteie? '))
cont = 0

print('-=' * 3, f'Sorteando {njog} Jogos'.upper(), '=-' * 3)

while cont != njog:
    jogos.clear()
    while len(jogos) < 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
    apostas.append(jogos[:])
    cont += 1
conta = 1
for a in apostas:
    sleep(1)
    print(f'Jogo {conta}: {sorted(a)}')
    conta += 1
print('-=' * 5, 'Boa Sorte'.upper(), '=-' * 5)
