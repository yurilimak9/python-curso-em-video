from datetime import date

print('-' * 23)
print('{:+^23}'.format(' Exercício 054 '))
print('-' * 23)

current_year = date.today().year
older_age = 0
younger_age = 0
for i in range(1, 8):
    year = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if current_year - year >= 18:
        older_age += 1
    else:
        younger_age += 1

print('Ao todo tivemos {} pessoas maiores de idade!'.format(older_age))
if younger_age > 0:
    print('E também tivemos {} pessoas menores de idade!'.format(younger_age))
else:
    print('E não tivemos nenhuma pessoa menor de idade!')