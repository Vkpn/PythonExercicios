def metade(pre, form=False):
    met = pre / 2
    if form:
        return f'R${met:.2f}'
    else:
        return met


def dobro(pre, form=False):
    dob = pre * 2
    if form:
        return f'R${dob:.2f}'
    else:
        return dob


def aumentar(pre, pora, form=False):
    aum = pre + pre * (pora / 100)
    if form:
        return f'R${aum:.2f}'
    else:
        return aum


def reduzir(pre, porr, form=False):
    red = pre - pre * (porr / 100)
    if form:
        return f'R${red:.2f}'
    return red


def moeda(moe):
    val = f'R${moe:.2f}'
    return val.replace('.', ',')


def resumo(pre, aum, red):
    print('-=-' * 11)
    print(f'{"Resumo do valor".upper():^33}')
    print('-=-' * 11)
    print(f'Preço analisado: {moeda(pre):>16}')
    print(f'Dobro do preço: {dobro(pre, True).replace(".", ","):>17}')
    print(f'Metade do preço: {metade(pre, True).replace(".", ","):>16}')
    print(f'{aum}% de aumento: {aumentar(pre, aum, True).replace(".", ","):>15}')
    print(f'{red}% de redução: {reduzir(pre, red, True).replace(".", ","):>15}')
    print('-=-' * 11)
