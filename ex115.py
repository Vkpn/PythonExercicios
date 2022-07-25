from moduloex115 import estrutura, dados, arquivo

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    estrutura.cabecalho('Menu Principal')
    op = dados.opcao('Sua Opção: ')
    if op == 1:
        arquivo.lerArquivo(arq)
    elif op == 2:
        estrutura.op2('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = dados.leiaInt('Idade: ')
        if idade == 'Cancel':
            continue
        else:
            arquivo.cadastrar(arq, nome, idade)
    else:
        estrutura.encerramento('Volte Sempre')
        break
