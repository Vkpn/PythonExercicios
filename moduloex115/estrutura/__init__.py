def cabecalho(msg):
    print('=' * 30)
    print(f'{msg:^30}'.upper())
    print('=' * 30)
    print('\033[33m1\033[m -> \033[34mVer Pessoas Cadastradas\033[m')
    print('\033[33m2\033[m -> \033[34mCadastrar Nova Pessoa\033[m')
    print('\033[33m3\033[m -> \033[34mSair do Sistema\033[m')
    print('=' * 30)


def op1(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)


def op2(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)


def encerramento(msg):
    from time import sleep
    print('Encerrando programa', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('=' * 30)
    print(f'\033[1;32m{msg}!')
