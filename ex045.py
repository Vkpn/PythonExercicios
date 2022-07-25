from random import choice
jog = str(input('Escolha: Pedra, Papel ou Tesoura? ')).lower().strip()
com = choice(['Pedra', 'Papel', 'Tesoura']).lower()

win = '\033[32m'
los = '\033[31m'

if jog == com:
    print('{} com {} dá empate!'.format(jog.upper(), com.upper()))
elif jog == 'pedra' and com == 'papel':
    print('{} com {} dá {}, você {}perdeu.'.format(jog.upper(), com.upper(), com.upper(), los))
elif jog == 'pedra' and com == 'tesoura':
    print('{} com {} dá {}, você {}ganhou.'.format(jog.upper(), com.upper(), jog.upper(), win))
elif jog == 'papel' and com == 'pedra':
    print('{} com {} dá {}, você {}ganhou.'.format(jog.upper(), com.upper(), jog.upper(), win))
elif jog == 'papel' and com == 'tesoura':
    print('{} com {} da {}, você {}perdeu.'.format(jog.upper(), com.upper(), com.upper(), los))
elif jog == 'tesoura' and com == 'pedra':
    print('{} com {} dá {}, você {}perdeu.'.format(jog.upper(), com.upper(), com.upper(), los))
elif jog == 'tesoura' and com == 'papel':
    print('{} com {} dá {}, você {}ganhou.'.format(jog.upper(), com.upper(), jog.upper(), win))



