nome = str(input('Digite seu nome completo: ')).strip()
print('Com todas as letras maiúsculas o nome fica: {}'.format(nome.upper()))
print('Com todas as letras minúsculas o nome fica: {}'.format(nome.lower()))
cort = nome.split()
print('O nome tem {} letras sem considerar os espaços.'.format(len(''.join(cort))))
print('O primeiro nome tem {} letras.'.format(len(cort[0])))





