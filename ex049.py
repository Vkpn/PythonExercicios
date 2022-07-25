t = int(input('Qual a tabuada que gostaria de ver? '))
n = int(input('Digite até qual multiplicador: '))
for c in range (0, n+1, 1):
    print('{} x {} = {}'.format(t, c, t * c))
print('FIM')