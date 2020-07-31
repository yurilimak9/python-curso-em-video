print('-' * 23)
print('{:+^23}'.format(' Exercício 056 '))
print('-' * 23)

mean = 0
older_man_name = ''
older_man_age = 0

amount_women = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    name = str(input('Nome: ')).strip().title()
    age = int(input('Idade: '))
    sex = str(input('Sexo: [M/F]')).strip().upper()

    if age > older_man_age and sex == 'M':
        older_man_name = name
        older_man_age = age

    if sex == 'F' and age < 20:
        amount_women += 1

    mean += age

print('A média de idade do grupo é de {:.1f} anos'.format(mean / 4))
if older_man_age > 0:
    print('O homem mais velho tem {} anos e se chama {}'.format(older_man_age, older_man_name))
if amount_women > 0:
    if amount_women == 1:
        print('Temos {} mulher com menos de 20 anos'.format(amount_women))
    else:
        print('Ao todo são {} mulheres com menos de 20 anos'.format(amount_women))
