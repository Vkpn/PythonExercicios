soma = contador = 0
print('Digite 999 para parar o programa')
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'A soma entre os {contador} números digitados é {soma}')