from random import sample
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
print('A sequencia para apresentação dos trabalhos é: {}'.format(sample((a1, a2, a3, a4), k=4)))