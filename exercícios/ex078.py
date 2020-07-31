print('-' * 23)
print('{:-^23}'.format(' Exercício 078 '))
print('-' * 23)

values = list()
for i in range(0, 5):
    num = int(input(f'Digite um valor para a posição {i}: '))
    values.append(num)

print(f'Você digitou os valores {values}')
print(f'O maior valor digitado foi {max(values)} nas posições', end=' ')
for index, value in enumerate(values):
    if max(values) == value:
        print(index, end='... ')

print(f'\nO menor valor digitado foi {min(values)} nas posições', end=' ')
for index, value in enumerate(values):
    if min(values) == value:
        print(index, end='... ')
