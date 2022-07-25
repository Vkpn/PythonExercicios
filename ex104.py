def leiaInt(c):
    if c.isnumeric():
        print(f'Você digitou o numero -> {c}')
    elif c.isalpha() or c.isspace() or c == '':
        print('\033[31mErro! Digite um número inteiro válido.\033[m')


while True:
    leiaInt(input('Digite um número: '))
