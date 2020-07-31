print('-' * 23)
print('{:-^23}'.format(' Exercício 062 '))
print('-' * 23)

term = int(input('Primeiro termo: '))
reason = int(input('Razão da PA: '))

counter = 1
limit = 10
while counter <= limit:
    print('{}'.format(term), end=' -> ')
    if counter == limit:
        print('PAUSA')

        limit += int(input('Quantos termos você quer mostrar a mais? '))

    term += reason
    counter += 1

print('Progressão finalizada com {} termos mostrados.'.format(limit))
