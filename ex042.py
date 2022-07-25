l1 = float(input('Digite a primeira face do triangulo: '))
l2 = float(input('Digite a segunda face do triangulo: '))
l3 = float(input('Digite a terceira face do triangulo: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    if l1 == l2 == l3:
        print('Com esses valores formamos um triangulo EQUILÁTERO.')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Com esses valores formamos um triangulo ISÓSCELES.')
    elif l1 != l2 != l3:
        print('Com esses valores podemos formar um triangulo ESCALENO.')
else:
    print('Com esses valores não podemos formar um triangulo.')
