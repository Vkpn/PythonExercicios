cont = 0
tot = 0
mai = 0
men = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um numero: '))
    if cont == 0:
        mai = num
        men = num
        cont += 1
        tot += num
    else:
        tot += num
        cont += 1
        if num > mai:
            mai = num
        elif num < men:
            men = num
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('~~' * 25)
print('Você digitou {} valores.'.format(cont))
print('A média dentre os valores digitados ficou: {:.2f}'.format(tot / cont))
print('O maior valor digitado foi: {}'.format(mai))
print('O menor valor digitado foi: {}'.format(men))

