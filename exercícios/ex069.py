print('-' * 23)
print('{:-^23}'.format(' Exercício 069 '))
print('-' * 23)

of_age = man = woman = woman_under_twenty = 0
while True:
    print('*' * 23)
    print('{:^23}'.format('CADASTRE UM PESSOA'))
    print('*' * 23)

    age = int(input('Idade: '))
    if age >= 18:
        of_age += 1

    while True:
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sex in 'MF':
            break
        print('Opção inválida! Tente novamente!')
    if sex == 'M':
        man += 1
    else:
        woman += 1
        if age < 20:
            woman_under_twenty += 1

    while True:
        response = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if response in 'SN':
            break
        print('Opção inválida! Tente novamente!')
    if response == 'N':
        break

print('=' * 45)
print(f'Total de pessoas com mais de 18 anos: {of_age}.')

# Quantidade de homens cadastrados
if man == 1:
    print(f'Ao todo temos {man} homem cadastrado.')
elif man > 1:
    print(f'Ao todo temos {man} homens cadastrados.')
else:
    print(f'Não temos nenhum homem cadastrado.')

# Mulheres com menos de 20 anos
if woman_under_twenty == 1:
    print(f'E temos {woman_under_twenty} mulher com menos de 20 anos.')
elif woman_under_twenty > 1:
    print(f'E temos {woman_under_twenty} mulheres com menos de 20 anos.')
else:
    print(f'Não temos nenhuma mulher com menos de 20 anos.')
