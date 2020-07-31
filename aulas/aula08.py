print('=' * 20)
print('{:^20}'.format('Aula 08'))
print('=' * 20)

from math import sqrt, ceil, floor
import random
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é igual a {raiz:.2f}')

num = random.randint(1, 10)
print(num)