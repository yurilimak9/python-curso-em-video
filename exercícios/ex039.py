from datetime import datetime

print('-' * 20)
print('{:^20}'.format('Exercício 039'))
print('-' * 20)

birth_year = int(input('Ano de nascimento: '))
sex = str(input('Qual seu sexo? [M/F]')).upper()

current_year = datetime.now().year
age = current_year - birth_year

print('Quem nasceu em {} tem {} anos em {}.'.format(birth_year, age, current_year))
if sex == 'M':
    if age < 18:
        print('''
    Ainda falta {} anos para o seu alistamento
    Seu alistamento será em {}.'''.format((18 - age), ((18 - age) + current_year)))
    elif age > 18:
        print('''
    Você já deveria ter se alistado há {} anos.
    Seu alistamento foi em {}.'''.format((age - 18), (current_year - (age - 18))))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sex == 'F':
    print('Você é mulher e não precisa se alistar')
else:
    print('Opção inválida. Tente novamente!')
