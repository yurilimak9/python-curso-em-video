print('-' * 23)
print('{:-^23}'.format(' Exercício 075 '))
print('-' * 23)

values = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))

print('+' * 30)
print(f'Você digitou os valores {values}')
print(f'O valor {values[0]} apareceu {values.count(values[0])} vezes')
print(f'O valor {values[1]} apareceu na {values.index(values[1]) + 1}ª posição')

print('Os valores pares digitados foram: ', end='')
for value in values:
    if value % 2 == 0:
        print(value, end=' ')
