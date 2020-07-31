print('-' * 23)
print('{:-^23}'.format(' Exercício 086 '))
print('-' * 23)

matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{j}]: ')))

print('-=' * 20)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end=' ')
    print()
