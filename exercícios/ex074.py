from random import randint

print('-' * 23)
print('{:-^23}'.format(' Exercício 074 '))
print('-' * 23)

values = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: ', end='')
for value in values:
    print(value, end=' ')

print(f'\nO maior valor sorteado foi {max(values)}')
print(f'O menor valor sorteado foi {min(values)}')
