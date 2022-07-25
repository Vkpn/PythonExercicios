valores = []
while len(valores) < 5:
    cont = 0
    val = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(val)
        print('Adicionado ao final da lista...')
    else:
        if val < min(valores):
            valores.insert(0, val)
            print('Adicionado na posição 0 da lista...')
        elif val > max(valores):
            valores.append(val)
            print('Adicionado ao final da lista...')
        else:
            while cont != len(valores):
                if val > valores[cont]:
                    cont += 1
                else:
                    valores.insert(cont, val)
                    print(f'Adicionado na posição {cont} da lista...')
                    break
print('-=-' * 18)
print(f'Os valores digitados em ordem foram: {valores}')