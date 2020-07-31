print('-' * 20)
print('{:^20}'.format('Exercício 033'))
print('-' * 20)

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

bigger = a
smaller = a

# Maior
if b > a and b > c:
    bigger = b
if c > a and c > b:
    bigger = c

# Menor
if b < a and b < c:
    smaller = b
if c < a and c < b:
    smaller = c

print('O MAIOR número é {} e o MENOR é {}'.format(bigger, smaller))
