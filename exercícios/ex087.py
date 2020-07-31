print('-' * 23)
print('{:-^23}'.format(' Exercício 087 '))
print('-' * 23)

matriz = [[], [], []]
even_sum = third_column = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{j}]')))

print('-=' * 20)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            even_sum += matriz[i][j]

        if j == 2:
            third_column += matriz[i][j]
    print()

print('-=' * 20)
print(f'A soma dos valores pares é {even_sum}.')
print(f'A soma dos valores da terceira coluna é {third_column}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
