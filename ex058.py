from random import randint
numcom = randint(0, 10)
tentativas = 1
print('=' * 60)
print('Tente adivinhar qual o numero que o computador pensou!!')
print('=' * 60)
palpite = int(input('Em qual numero de 0 a 10 o computador pensou? '))
while palpite != numcom:
    palpite = int(input('Errado, tente novamente: '))
    tentativas +=1
print('=' * 60)
print('O numero escolhido foi {}'.format(numcom))
print('Você utilizou {} tentativas.'.format(tentativas))
