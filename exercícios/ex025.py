print('-' * 20)
print('{:^20}'.format('Exercício 025'))
print('-' * 20)

name = str(input('Digite seu nome completo: '))

print('No nome {} possui a palavra "Silva"? {}'.format(name.title().strip(), "SILVA" in name.upper().split()))
