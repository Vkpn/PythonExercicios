from datetime import date
nas = int(input('Qual o ano que você nasceu? '))
ali = date.today().year - nas
tem = ali - 18

if ali > 18:
    print('Cuidado! Já passou {} anos do seu periodo de alistamento.'.format(tem))
elif ali < 18:
    print('Ainda não está na hora de se alistar, faltam {} anos para seu alistamento.'.format(tem * -1))
else:
    print('Providencie o seu alistamento o mais breve possivel.')
