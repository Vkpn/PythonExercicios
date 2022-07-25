from datetime import date
ano = date.today().year

mediaidade = 0
idadehold = 0
mcont = 0

for count in range(0, 4):
    nomet = str(input('Digite o nome da {} pessoa: '.format(count + 1)))
    idadet = (int(input('Digite o ano de nascimento da {} pessoa: '.format(count + 1))) - ano) * -1
    sexo = str(input('Sexo da {} pessoa [ M ] para masculino e [ F ] para feminino: '.format(count + 1).lower()))
    print('=' * 50)

    mediaidade += idadet

    if sexo == 'm':
        if idadet > idadehold:
            idadehold = idadet
            nome = nomet

    if sexo == 'f' and idadet < 20:
        mcont += 1

print('A média de idade das pessoas é {:.1f}'.format(mediaidade / 4))
print('O nome do homem mais velho é: {}'.format(nome.title()))
print('O grupo tem {} mulheres menores de 20 anos.'.format(mcont))
