tabela = ('Corinthians', 'Atlético Mineiro', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avaí', 'América', 'Palmeiras', 'Bragantino',
          'Internacional', 'Fluminense', 'Goiás', 'Cuiaba', 'Atlético Paranaense', 'Flamengo', 'Juventude', 'Ceará', 'Atlético Goianiense', 'Fortaleza')
for cont in range(0, 5):
    print(f'O {cont + 1}° colocado é: {tabela[cont]}')
print('~~' * 20)
for contul in range(-4, 0):
    print(f'O {contul + 21}° colocado é: {tabela[contul]}')
print('~~' * 20)
print(sorted(tabela))
print('~~' * 20)
time = str(input('Digite o nome do time para saber sua posição: ')).strip().title()
while time not in tabela:
    time = str(input('Este time não está na primeira divisão. Digite outro time: ')).strip().title()
print(f'O {time} está na {tabela.index(time) + 1}° posição.')