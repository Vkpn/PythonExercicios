from random import randint
from time import sleep


def sorteia(n):
    for c in range(0, 5):
        sort = randint(0, 9)
        num.append(sort)
    print(f'Sorteando 5 valores da lista: ->', end=' ')
    for i in num:
        sleep(0.3)
        print(i, end=' ')
    print('<-')


def somaPar(s):
    som = 0
    for i in num:
        if i % 2 == 0:
            som += i
    print(f'Somando os valores pares de {num} temos {som}.')


num = []
sorteia(num)
somaPar(num)
