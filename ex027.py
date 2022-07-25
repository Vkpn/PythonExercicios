nome = str(input('Escreva seu nome completo: ').title()).strip()
print(nome)
nfat = nome.split()

print('Primeiro nome: {}'.format(nfat[0]))
print('Ultimo nome: {}'.format(nfat[-1]))

#cont = len(nfat) - 1
#print('Ultimo nome: {}'.format(nfat[cont]))