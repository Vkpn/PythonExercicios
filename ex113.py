def leiaInt(msg):
    while True:
        try:
            numi = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
        else:
            return numi


def leiaReal(msg):
    while True:
        try:
            numr = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO: Digite um número real válido.\033[m')
        else:
            return numr


inteiro = leiaInt('Digite um valor inteiro: ')
real = leiaReal('Digite um valor real: ')
print('-=-' * 20)
print(f'O valor inteiro digitado foi: {inteiro}')
print(f'O valor real digitado foi: {real}')
