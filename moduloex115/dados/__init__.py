def opcao(msg):
    while True:
        try:
            op = int(input(f'\033[32m{msg}\033[m'))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            break
        else:
            if 0 < op < 4:
                return op
            else:
                print(f'\033[31mERRO: {op} não é uma opção válida.\nPor favor, digite uma opção válida.\033[m')


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mCancelando cadastro.\033[m')
            return 'Cancel'
        except:
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
        else:
            return num
