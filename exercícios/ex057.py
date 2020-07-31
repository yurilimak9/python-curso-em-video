print('-' * 23)
print('{:+^23}'.format(' Exercício 057 '))
print('-' * 23)

sex = str(input('Informe seu sexo: [M/F] ')).upper()

if sex != 'M' and sex != 'F':
    while sex != 'M' and sex != 'F':
        sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()

print('Sexo {} registrado com sucesso!'.format(sex))
