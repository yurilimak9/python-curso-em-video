print('-' * 20)
print('{:^20}'.format('Exercício 038'))
print('-' * 20)

first_number = int(input('Primeiro número: '))
last_number = int(input('Segundo número: '))

if first_number > last_number:
    print('PRIMEIRO valor é maior!')
elif last_number > first_number:
    print('SEGUNDO valor é maior!')
else:
    print('Os valores são IGUAIS!')
