aluno = {'nome': str(input('Nome do aluno: ')).title().strip(), 'media': float(input('Média do aluno: '))}
if aluno['media'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('=' * 20)
print(f'O nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situação"]}')
