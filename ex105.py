def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: um ou mais notas dos alunos (aceita várias)
    :param sit: mostra um panorama da situação da turma (valor opcional)
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resumo = {'total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': sum(n) / len(n)}
    if sit:
        if resumo['Média'] >= 7.0:
            resumo['Situação'] = 'Boa'
        elif resumo['Média'] >= 5.0:
            resumo['Situação'] = 'Razoável'
        else:
            resumo['Situação'] = 'Ruim'
    return resumo


# Programa principal
print(notas(3.5, 2, 6.5, 2, 7, 4, sit=True))
