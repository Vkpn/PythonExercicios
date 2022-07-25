sex = ''
while sex != 'm' and sex != 'f':
    sex = str(input('Qual seu sexo? [M/F] ')).lower().strip()
if sex == 'm':
    print('Bom dia Sr!')
elif sex == 'f':
    print('Bom dia Sra!')