print('-' * 20)
print('{:^20}'.format('Exercício 027'))
print('-' * 20)

# name = str(input('Digite seu nome completo: '))
#
# print('Muito prazer em te conhcer!')
# print('Primeiro nome: {}'.format(name.title().split()[0]))
# print('Útimo nome: {}'.format(name.title().split()[-1]))

test = 'Yuri    Gonçalves  LIma'
result = ' '.join(test.strip().split()).title()
print(test)
print(result)
