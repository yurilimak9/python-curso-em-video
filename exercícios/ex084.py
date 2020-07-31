print('-' * 23)
print('{:-^23}'.format(' Exercício 084 '))
print('-' * 23)

people = list()
data = list()
while True:
    data.append(str(input('Nome: ')).strip().title())
    data.append(float(input('Peso: ')))
    people.append(data.copy())
    data.clear()

    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if option in 'SN':
            break
        print('Opção inválida. Tente novamente!')
    if option == 'N':
        break

max = min = 0
for index, p in enumerate(people):
    if index == 0:
        max = min = p[1]
    else:
        if p[1] > max:
            max = p[1]

        if p[1] < min:
            min = p[1]

print("-" * 60)

print(people)
print(f'Ao todo, você cadastrou {len(people)} pessoas')
print(f'O maior peso foi de {max:.2f}. Peso de', end=' ')
for p in people:
    if p[1] == max:
        print(f'{p[0]}', end='... ')

print(f'\nO menor peso foi de {min:.2f}. Peso de', end=' ')
for p in people:
    if p[1] == min:
        print(f'{p[0]}', end='... ')
