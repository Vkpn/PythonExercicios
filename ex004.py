n = input('Digite algo: ')
print('O tipo primitivo de {} é: '.format(n), type(n))
print('{} tem'.format(n), len(n), 'letras.')
print('{} é formado somente de espaços? '.format(n), n.isspace())
print('{} é um número? '.format(n), n.isnumeric())
print('{} é Alfabético? '.format(n), n.isalpha())
print('{} é  alfanumérico? '.format(n), n.isalnum())
print('{} está totalmente em letras maiúsculas? '.format(n), n.isupper())
print('{} está somente em letras minúsculas? '.format(n), n.islower())
print('Está captalizada? '.format(n), n.istitle())






