from math import factorial

print('-' * 23)
print('{:+^23}'.format(' Exercício 060 '))
print('-' * 23)

num = int(input('Digite um número para calcular seu Fatorial: '))

factorial = factorial(num)
print('Calculando {}! = '.format(num), end='')
while num >= 1:
    if num > 1:
        print(num, end=' x ')
    else:
        print(num, end=' = ')
    num -= 1

print('{}'.format(factorial))
