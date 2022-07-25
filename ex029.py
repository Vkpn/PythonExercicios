vel = int(input('Qual a velocidade do carro em Km/h? '))
if vel <= 80:
    print('Boa viajem.')
else:
    print('Sua velocidade foi {}Km/h, está {}Km/h acima da velocidade permitida!'.format(vel, vel - 80))
    print('Sua multa é de R$ {:.2f}'.format((vel - 80) * 7))
