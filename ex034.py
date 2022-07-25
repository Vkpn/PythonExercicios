sal = float(input('Qual o valor do seu salário? R$ '))
if sal > 1250.00:
    print('O valor do seu salario com o aumento fica em {:.2f}'.format(sal*10/100 + sal))
else:
    print('O valor do seu salario com o aumento fica em {:.2f}'.format(sal*15/100 + sal))
