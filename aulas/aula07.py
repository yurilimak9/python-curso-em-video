print('=' * 20)
print('{:^20}'.format('Aula 07'))
print('=' * 20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end=' - ')
print('Divisão inteira {} e potência {}'.format(di, e))