print('Digite 0 para encerrar o programa.')
while True:
    mul = 0
    print('~' * 30)
    tab = int(input('Gostaria de ver a tabuada de qual valor? '))
    print('~' * 30)
    if tab == 0:
        break
    if tab < 0:
        tab *= -1
    while mul <= 10:
        print(f'{tab} x {mul:2} = {tab * mul}')
        mul += 1
print('Programa encerrado.')
