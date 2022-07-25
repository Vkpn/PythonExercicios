nome = input('Qual o nome do Aluno? ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('O aluno {}, obteve {} na primeira nota e {} na segunda nota, portanto sua média é: {:.1f}'.format(nome, n1, n2, (n1+n2)/2))
