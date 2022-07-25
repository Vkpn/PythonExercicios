from utilidadeCeV import moeda
p = float(input('Digite o preço do produto: '))
print(f'A metade de {p} é {moeda.metade(p)} ')
print(f'O dobro de {p} é {moeda.dobro(p)}')
poa = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando o preço de {p} em {poa}%, temos {moeda.aumentar(p, poa)}')
por = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo o preço de {p} em {por}%, temos {moeda.reduzir(p, por)}')
