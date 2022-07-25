from time import sleep


def maior(* num):
    print('-=' * 32)
    print('Analisando os valores passados...', end=' ')
    for n in num:
        sleep(0.8)
        print(n, end='... ')
    sleep(0.5)
    print(f'\nForam informados {len(num)} valores ao todo.')
    sleep(.5)
    if len(num) != 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Não exite valor informado.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
