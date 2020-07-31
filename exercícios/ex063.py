print('-' * 23)
print('{:-^23}'.format(' Exercício 063 '))
print('-' * 23)

print('*' * 30)
print('*{:^28}*'.format('Sequência de Fibonacci'))
print('*' * 30)

terms = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')

counter = 2
while counter < terms:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    counter += 1

print(' - FIM')
