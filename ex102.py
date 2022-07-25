def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número:
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar a conta ou não.
    :return: O valor fatorial de um número n.
    """
    if not show:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        return f


# Programa principal
val = int(input('Digite um valor: '))
while True:
    ver = str(input('Gostaria de ver o processo? [S/N] '))[0].upper().strip()
    if ver in 'Nn':
        ver = False
        break
    else:
        while ver not in 'NnSs':
            ver = str(input('Opção inválida. Gostaria de ver o processo? [S/N]'))[0].upper().strip()
        if ver in 'Nn':
            ver = False
            break
    ver = True
    break

print(fatorial(val, ver))
