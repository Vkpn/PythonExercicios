jogador = {}
gpp = []
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1, part + 1):
    gpp.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = gpp[:]
jogador['total de gols'] = sum(gpp)
print('=' * 50)
print(jogador)
print('=' * 50)
for d, v in jogador.items():
    print(f'{d.upper():<13}:', f'{str(v)}')
print('=' * 50)
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for p in range(1, part + 1):
    print(f'Na partida {p}, fez {jogador["gols"][p-1]} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')
