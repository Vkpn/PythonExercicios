turma = []
aluno = []
notas = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    notas.append(media)
    aluno.append(nome)
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar in 'Nn':
        break
    else:
        while continuar not in 'NnSs':
            continuar = str(input('Opção inválida. Deseja continuar? [S/N]')).upper().strip()
    if continuar in 'Nn':
        break
print('==' * 30)
print('No.', f'{"Nome":<20}'.upper(), 'Média'.upper())
for a in turma:
    print(f'{turma.index(a):<3}', end=' ')
    print(f'{a[0]:<20}'.title(), end=' ')
    print(f'{a[1][2]:.1f}')
print('==' * 30)
while True:
    alu = int(input('Mostrar as notas de qual aluno? (999 finaliza): '))
    if alu == 999:
        break
    else:
        print(f'As notas da {turma[alu][0].title()} foram {turma[alu][1][0]} e {turma[alu][1][1]}.')
        print('==' * 30)
print('Finalizando...')