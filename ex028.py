import random
num = int(random.randrange(0, 6))
esc = int(input('Tente acertar o numero entre 0 e 5: '))
if num == esc:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou.')
print('=' * 10 + 'FIM' + '=' * 10)
