print('=' * 20)
print('{:^20}'.format('Exercício 006'))
print('=' * 20)

from math import sqrt

num = int(input('Digite um número: '))

print(f'Informações sobre o número {num}: ')
print(f'Seu dobro é {num * 2}; \nSeu triplo é {num * 3}; \nSua raiz quadrada é {sqrt(num):.2f};')