print('-' * 23)
print('{:+^23}'.format(' Exercício 061 '))
print('-' * 23)

print('*' * 21)
print('*{:^19}*'.format(' Gerador de PA '))
print('*' * 21)

term = int(input('Primeiro termo: '))
reason = int(input('Razão da PA: '))

counter = 1
while counter <= 10:
    print('{}'.format(term), end=' -> ')
    term += reason
    counter += 1

print('FIM')
