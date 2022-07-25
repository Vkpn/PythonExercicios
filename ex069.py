form = str('cadastre uma pessoa').upper()
print('-' * 30)
print(f'{form:^30}')
print('-' * 30)
mai = hom = mul20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo: [M/F] ')).strip()[0]
    if idade > 18:
        mai += 1
    if sexo in 'Mm':
        hom += 1
    if sexo in 'Ff' and idade < 20:
        mul20 += 1
    print(' ~ ' * 10)
    print('Cadastro realizado com sucesso!')
    print(' ~ ' * 10)
    cont = str(input('Deseja continuar? [S/N] ')).strip()[0]
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if cont in 'Nn':
        break
print('\033[31m++++++ Programa finalizado. ++++++\033[m')
print(f'Total de pessoas com mais de 18 anos: {mai}')
print(f'Ao todo temos {hom} homens cadastrados')
print(f'Temos {mul20} mulher com menos de 20 anos')
