valores = []
cont = 's'
while cont in 'Ss':
    while cont in 'Ss':
        val = int(input('Digite um valor: '))
        if val not in valores:
            valores.append(val)
            print(f'Valor {val} adicionado com sucesso!')
            cont = str(input('Você quer continuar? [S/N] '))
        elif val in valores:
            print(f'Valor {val} já adicionado, insira outro número.')
            cont = str(input('Você quer continuar? [S/N] '))
        while cont not in 'NnSs':
            cont = str(input('Você quer continuar? [S/N] '))
        if cont in 'Nn':
            break
print(f'Você digitou os valores: {sorted(valores)}')
