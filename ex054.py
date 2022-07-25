from datetime import date
men = 0
mai = 0
ano = date.today().year
for c in range(0, 7):
    dat = int(input('Digite o ano de nascimento da {} pessoa: '.format(c + 1)))
    if ano - dat < 21:
        men += 1
    else:
        mai += 1
print('{} pessoas são maior de idade.'.format(mai))
print('{} pessoas são menor de idade.'.format(men))
