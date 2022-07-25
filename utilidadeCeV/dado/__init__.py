def leiaDinheiro(valor):
    uni = input(valor).replace(',', '.').strip()
    if uni.isnumeric():
        return float(uni)
    while True:
        if uni.isalpha() or uni.isspace() or uni == '':
            print(f'\033[31mERRO: \"{uni}\" é um preço inválido!\033[m')
            uni = input(valor).replace(',', '.').strip()
        else:
            break
    return float(uni)


def leiaPorcentagem(valor):
    uni = input(valor).replace(',', '.').strip()
    if uni.isnumeric():
        return float(uni)
    while True:
        if uni.isalpha() or uni.isspace() or uni == '':
            print(f'\033[31mERRO: \"{uni}\" é uma porcentagem inválida!\033[m')
            uni = input(valor).replace(',', '.').strip()
        else:
            break
    return float(uni)
