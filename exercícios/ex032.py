from datetime import date

print('-' * 20)
print('{:^20}'.format('Exercício 032'))
print('-' * 20)

year = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(year))
else:
    print('O ano {} não é BISSEXTO!'.format(year))
