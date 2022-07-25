from utilidadeCeV import moeda
p = float(input('Digite o preço do produto: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)} ')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
poa = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando o preço de {moeda.moeda(p)} em {poa}%, temos {moeda.aumentar(p, poa, True)}')
por = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo o preço de {moeda.moeda(p)} em {por}%, temos {moeda.reduzir(p, por, True)}')
