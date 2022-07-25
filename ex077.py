lista = ('aprender', 'programar', 'futuro', 'sucesso', 'trabalho', 'emprego', 'carreira', 'feliz', 'praticar', 'estudar', 'mercado', 'reconhecimento', 'valor', 'salario')
for cont in range(0, len(lista)):
    pal = lista[cont].upper()
    print(f'\nNa palavra {pal} temos as seguintes vogais: ', end='')
    for c in range(0, len(pal)):
        if pal[c] in 'AEIOU':
            print(pal[c], end=' ')
