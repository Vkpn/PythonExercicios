from time import sleep


def cabe(i):
    print('\033[1;42m=' * (len(i) + 6))
    print(f'\033[1;42m-- {i} --')
    print('\033[1;42m=' * (len(i) + 6))


def msg(i):
    print('\033[1;44m=' * (len(i) + 6))
    print(f'\033[1;44m-- {i} --')
    print('\033[1;44m=' * (len(i) + 6))


def ajuda(i):
    help(i)


def saida(i):
    print('\033[1;41m=' * (len(i) + 6))
    print(f'\033[1;41m-- {i} --')
    print('\033[1;41m=' * (len(i) + 6))


item = ''
while item != 'fim':
    cabe('Sistema de ajuda PyHelp'.title())
    item = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if item == 'fim':
        sleep(1.2)
        break
    msg(f'Acessando o manual do comando \'{item}\'')
    sleep(1.2)
    print('\033[30;107m', end='')
    ajuda(item)
    print('\033[m', end='')
saida('Até Mais!'.upper())
