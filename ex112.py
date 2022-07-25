from utilidadeCeV import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
a = dado.leiaPorcentagem('Digite a porcentagem a ser acrescida: ')
d = dado.leiaPorcentagem('Digite a porcentagem a ser retirada: ')
moeda.resumo(p, a, d)
