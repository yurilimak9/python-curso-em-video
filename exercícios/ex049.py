print('-' * 23)
print('{:+^23}'.format(' Exercício 049 '))
print('-' * 23)

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    print('{} x {:>2} = {}'.format(num, i, (num * i)))
