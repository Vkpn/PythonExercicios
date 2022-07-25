num = []
while True:
    num.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont in 'Nn':
        break
    else:
        while cont not in 'SsNn':
            cont = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
    if cont in 'Nn':
        break
print(f'Foram digitados {len(num)} números.')
print(f'Valores ordenados de forma decrescente: {sorted(num, reverse=True)}')
if 5 in num:
    print(f'O valor 5 faz parte da lista e foi digitado {num.count(5)} vezes.')
    print(f'A posição dos valores 5 são:', end=' ')
    for c, v in enumerate(num):
        if v == 5:
            print(c, end=' ')
else:
    print('O valor 5 não faz parte da lista.')
