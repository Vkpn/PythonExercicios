lista = []
listapar = []
listaimp = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
    else:
        while cont not in 'SsNn':
            cont = str(input('Opção inválida. Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
for val in lista:
    if val % 2 == 0:
        listapar.append(val)
    else:
        listaimp.append(val)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores digitados em ordem crescente foram: {sorted(lista)}')
print(f'Os valores pares digitados foram: {listapar}')
print(f'Os valores impares digitados foram: {listaimp}')
