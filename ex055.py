mai = 0
men = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {} pessoa: '.format(c+1)))
    if c == 1:
        mai = peso
        men = peso
    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso
print('A pessoa mais pesada tem {}Kg'.format(mai))
print('A pessoa mais leve tem {}Kg'.format(men))
