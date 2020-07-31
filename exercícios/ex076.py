print('-' * 23)
print('{:-^23}'.format(' Exercício 076 '))
print('-' * 23)

print('*' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('*' * 40)

products = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

for index, product in enumerate(products):
    if index % 2 == 0:
        print('{:.<20}R$'.format(product), end=' ')
    else:
        print('{:>6.2f}'.format(product))
