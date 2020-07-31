print('-' * 23)
print('{:+^23}'.format(' Exercício 052 '))
print('-' * 23)

num = int(input('Digite um número: '))

is_cousin = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;32m{}\033[m'.format(i), end=' ')
        is_cousin += 1
    else:
        print('\033[1;33m{}\033[m'.format(i), end=' ')

print('\nO número {} foi divisível {} vezes'.format(num, is_cousin))
if is_cousin == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
