from utilidadeCeV import moeda
p = float(input('Digite o preço do produto: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))} ')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
poa = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando o preço de {moeda.moeda(p)} em {poa}%, temos {moeda.moeda(moeda.aumentar(p, poa))}')
por = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo o preço de {moeda.moeda(p)} em {por}%, temos {moeda.moeda(moeda.reduzir(p, por))}')
