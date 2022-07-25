def ficha(n, g):
    if n in '':
        n = str('<Desconhecido>')
    if g in '' or g.isalpha():
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('=' * 30)
nome = str(input('Nome do jogador: ')).strip().title()
gols = input('Gols marcados: ')
ficha(nome, gols)
