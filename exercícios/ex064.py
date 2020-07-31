print('-' * 23)
print('{:-^23}'.format(' Exercício 064 '))
print('-' * 23)

total = counter = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += num
        counter += 1

print('Você digitou {} números e a soma entre eles foi {}.'.format(counter, total))
