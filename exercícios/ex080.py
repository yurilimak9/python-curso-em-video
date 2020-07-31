print('-' * 23)
print('{:-^23}'.format(' Exercício 080 '))
print('-' * 23)

values = list()
for i in range(5):
    num = int(input('Digite um valor: '))
    if i == 0 or num >= values[-1]:
        values.append(num)
        print('Adicionado no final da lista...')
    else:
        for j in range(len(values)):
            if num <= values[j]:
                values.insert(j, num)
                print(f'Adicionado na posição {j} da lista...')
                break

print('*' * 40)
print(f'Os valores digitados em ordem foram {values}')