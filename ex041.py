from datetime import date
ida = int(input('Qual o ano de nascimento do atleta? '))
san = date.today().year
cat = san - ida

if cat <= 9:
   print('Atleta categoria: MIRIM ({} anos)'.format(cat))
elif cat <= 14:
   print('Atleta categoria: INFANTIL ({} anos)'.format(cat))
elif cat <= 19:
   print('Alteta categoria: JUNIOR ({} anos)'.format(cat))
elif cat <= 25:
   print('Atleta categoria: SENIOR ({} anos)'.format(cat))
else:
   print('Atleta categoria: MASTER ({} anos)'.format(cat))
