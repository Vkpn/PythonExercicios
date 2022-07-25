from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        while inicio <= fim:
            sleep(0.3)
            print(inicio, end=' ')
            inicio += abs(passo)
    elif fim < inicio:
        while fim <= inicio:
            sleep(0.3)
            print(inicio, end=' ')
            inicio -= abs(passo)
    elif inicio == fim:
        print(inicio, end=' ')
    sleep(0.5)
    print('Fim!')
    print('-=-' * 10)


print('-=-' * 10)
contador(1, 10, 1)
contador(10, 0, 2)
contador(inicio=int(input('Inicio: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))
