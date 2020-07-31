from math import trunc

print('=' * 20)
print('{:^20}'.format('Exercício 016'))
print('=' * 20)

num = float(input('Digite um valor: '))

print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')

# Outra forma de fazer
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')
