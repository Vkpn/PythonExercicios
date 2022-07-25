from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
dados['idade'] = datetime.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Numero da CTPS: [0 caso não tenha] '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.today().year) + dados['idade']
print('=' * 40)
print(f'{"dados".upper():^40}')
print('=' * 40)
for dad, val in dados.items():
    print(f'{dad.upper()}: {val}')
