dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual a distancia em quilometros percorrida com o carro? '))
print('Total a pagar é de R${:.2f}'.format((dias*60)+(km*0.15)))
