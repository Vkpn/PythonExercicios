time = []
jogador = {}
gpp = []
while True:
    print('=' * 70)
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, part + 1):
        gpp.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = gpp[:]
    jogador['total de gols'] = sum(gpp)
    time.append(jogador.copy())
    jogador.clear()
    gpp.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont in 'Nn':
        break
    else:
        while cont not in 'NnSs':
            cont = str(input('Opção inválida, Deseja continuar? [S/N] ')).upper()
        if cont in 'Nn':
            break
print('=' * 70)
print(f'{"Cod.":<5}{"Nome":<20}{"Gols":<40}{"Total":<6}')
print('=' * 70)
for c, j in enumerate(time):
    print(f'{c:<5}', end='')
    print(f'{time[c]["nome"]:<20}', end='')
    print(f'{str(time[c]["gols"]):<40}', end='')
    print(f'{time[c]["total de gols"]:<6}')
print('=' * 70)
while True:
    dados = int(input('Detalhar qual jogador? [999 = SAIR] '))
    if dados == 999:
        break
    else:
        while dados >= len(time) and dados != 999:
            dados = int(input('Código inválido. Detalhar qual jogador? '))
            print('=' * 70)
        if dados == 999:
            break
    print(f'- Levantamento do jogador {time[dados]["nome"]}:')
    for p in time[dados]['gols']:
        print(f'No jogo {time[dados]["gols"].index(p)+1} {time[dados]["nome"]} fez {p} gols.')
    print('=' * 70)
print('Finalizando...')
