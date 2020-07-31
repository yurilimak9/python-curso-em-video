print('-' * 20)
print('{:^20}'.format('Exercício 035'))
print('-' * 20)

print('-=-' * 20)
print('{:^60}'.format('ANALISADOR DE TRIÂNGULOS'))
print('-=-' * 20)

a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))

# Formúla
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('Com os três segmentos de reta {}, {} e {}, podemos formar um triângulo!'.format(a, b, c))
else:
    print('Com os três segmentos de reta {}, {} e {}, NÂO podemos formar um triângulo!'.format(a, b, c))
