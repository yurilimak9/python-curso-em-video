from math import hypot

print('=' * 20)
print('{:^20}'.format('Exercício 017'))
print('=' * 20)

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

# Outra forma de fazer
hi = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
