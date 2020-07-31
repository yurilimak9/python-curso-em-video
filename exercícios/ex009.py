print('=' * 20)
print('{:^20}'.format('Exercício 009'))
print('=' * 20)

num = int(input('Digite um número inteiro: '))

print('-' * 30)
print('{:^30}'.format('TABUADA'))
print('-' * 30)

for n in range(0, 11):
    print('{:>2} x {} = {}'.format(n, num, num * n))

print('-' * 30)