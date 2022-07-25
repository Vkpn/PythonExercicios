grupo = []
pessoa = {}
med = []
mulheres = []

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] in 'MmFf':
            break
        print('Opção inválida. Digite apenas "M" para masculino ou "F" para feminino.')
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    med.append(pessoa['idade'])
    grupo.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Deseja continuar? [S/N] ')).strip()
    if cont in 'Nn':
        break
    else:
        while cont not in 'NnSs':
            cont = str(input('Opção inválida. Deseja continuar? '))
        if cont in 'Nn':
            break

print('=' * 40)
print(f'- Foram cadastradas {len(grupo)} pessoas.')
print(f'- A média de idade é {sum(med) / len(med):.2f} anos. ')
print(f'- As mulheres cadastradas foram: ', end='')
for p in mulheres:
    print(p, end=' ')
print('\n- Lista de pessoas que estão acima da média de idade:')
for p in grupo:
    if p['idade'] > (sum(med) / len(med)):
        print(p['nome'], 'com', end=' ')
        print(p['idade'], 'anos')
