print('=' * 20)
print('{:^20}'.format('Exercício 007'))
print('=' * 20)

first_note = float(input('Digite a primeira nota: '))
second_note = float(input('Digite a segunda nota: '))

media = (first_note + second_note) / 2

print(f'A média entre {first_note} e {second_note} é igual a {media:.1f}')