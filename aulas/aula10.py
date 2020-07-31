print('=' * 20)
print('{:^20}'.format('AULA 10'))
print('=' * 20)

name = str(input('Qual é seu nome? ')).title().strip()

if name == 'Yuri':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(name))

