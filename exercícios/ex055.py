print('-' * 23)
print('{:+^23}'.format(' Exercício 055 '))
print('-' * 23)

max = 0
min = 0
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso

        if peso < min:
            min = peso

print('''
O maior peso lido foi de {}Kg
O menor peso lido foi de {}Kg'''.format(max, min))
