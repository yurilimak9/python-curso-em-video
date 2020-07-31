from datetime import  datetime

print('-' * 20)
print('{:^20}'.format('Exercício 041'))
print('-' * 20)

birth_year = int(input('Ano de nascimento: '))

age = datetime.now().year - birth_year

print('O atleta tem {} anos.'.format(age))

if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificão: INFANTIL')
elif age <= 19:
    print('Classificação: JÚNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
