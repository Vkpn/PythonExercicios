from random import randint
computador = randint(0, 10)
print('-=-' * 9)
print('Vamos jogar par ou impar!'.upper())
print('-=-' * 9)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    parimp = str(input('Par ou Ímpar? [P/I] ')).strip()
    while parimp not in 'PpIi':
        parimp = str(input('Par ou Ímpar? [P/I] ')).strip()
    if parimp in 'Pp':
        if (jogador + computador) % 2 == 0:
            vitorias += 1
            print('---' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} é PAR')
            print('---' * 15)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=-' * 9)
        else:
            print('---' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} é IMPAR')
            print('---' * 15)
            print('Você Perdeu!')
            break
    elif parimp in 'Ii':
        if (jogador + computador) % 2 != 0:
            vitorias += 1
            print('---' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} é IMPAR')
            print('---' * 15)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=-' * 9)
        else:
            print('---' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} é PAR')
            print('---' * 15)
            print('Você Perdeu!')
            break
print('-=-' * 9)
print(f'GAME OVER! Você conseguiu vencer um total de {vitorias} vezes seguidas!')