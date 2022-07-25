def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Voto negado!'
    elif idade < 18:
        return f'Com {idade} anos: Voto opcional!'
    elif idade < 65:
        return f'Com {idade} anos: Voto obrigatório!'
    else:
        return 'Voto opcional!'


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
