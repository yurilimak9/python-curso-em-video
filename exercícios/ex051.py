print('-' * 23)
print('{:+^23}'.format(' Exercício 051 '))
print('-' * 23)

print('=' * 31)
print('{:=^31}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 31)

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first_term + (10 - 1) * reason

for i in range(first_term, tenth + 1, reason):
    print('{} -> '.format(i), end='')

print('ACABOU')
