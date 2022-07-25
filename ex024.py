cid = str(input('Digite o nome de uma cidade: ')).strip()
print('O nome dessa cidade começa com "SANTO"? {}'.format(bool(cid.upper().count('SANTO', 0, 5))))


