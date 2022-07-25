pessoas = []
dados = []
pesa = []
leve = []
totpes = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    totpes += 1
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
    else:
        while cont not in 'NnSs':
            cont = str(input('Opção inválida, deseja continuar? '))
        if cont in 'Nn':
            break
for n, p in pessoas:
    if p > 100:
        pesa.append(n)
    elif p < 60:
        leve.append(n)
print('~' * 30)
print(f'Foram cadastradas um total de {totpes} pessoas.')
print(f'Com mais de 100Kg: ', end='')
for n in pesa:
    print(n, end=' ')
print(f'\nCom menos de 60Kg: ', end='')
for n in leve:
    print(n, end=' ')
