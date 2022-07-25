n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2

if med < 5.0:
    print('Reprovado.')
elif med >= 7.0:
    print('Aprovado.')
else:
    print('Recuperação.')