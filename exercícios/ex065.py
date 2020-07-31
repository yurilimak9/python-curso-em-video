print('-' * 23)
print('{:-^23}'.format(' Exercício 065 '))
print('-' * 23)

quantity = total = max = min = 0
proceed = 'S'
while proceed == 'S':
    num = int(input('Digite um número: '))
    if quantity == 0:
        max = min = num
    else:
        if num > max:
            max = num

        if num < min:
            min = num

    quantity += 1
    total += num
    proceed = str(input('Quer continuar? [S/N] ')).upper()

print('Você digitou {} números e a média foi {:.2f}'.format(quantity, (total / quantity)))
print('O maior valor foi {} e o menor foi {}'.format(max, min))
