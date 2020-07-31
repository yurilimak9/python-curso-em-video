print('-' * 20)
print('{:^20}'.format('Exercício 022'))
print('-' * 20)

name = str(input('Digite seu nome completo: '))

print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}'.format(name.upper()))
print('Seu nome em minúscalas: {}'.format(name.lower()))
print('Seu nome tem {} letras!'.format(len(name.replace(' ', ''))))
print('Seu primeiro nome tem {} letras!'.format(len(name.split()[0])))
