dist = float(input('Qual a distancia da viagem em Km? '))
if dist < 200:
    print('O valor a ser pago pela viagem é: RS{:.2f}'.format(dist*0.5))
else:
    print('O valor a ser pago pela viagem é: R${:.2f}'.format(dist*0.45))