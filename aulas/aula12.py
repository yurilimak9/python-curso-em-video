print('=' * 20)
print('{:^20}'.format('AULA 12'))
print('=' * 20)

name = str(input('Qual é seu nome? ')).title().strip()

if name == 'Yuri':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif name in "Ana Claúdia Jéssica Juliana":
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(name))
