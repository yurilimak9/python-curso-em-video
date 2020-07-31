print('-' * 23)
print('{:-^23}'.format(' Exercício 066 '))
print('-' * 23)

counter = sum = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break

    sum += num
    counter += 1

if counter == 1:
    print(f'Você informou apenas o valor {sum}.')
elif counter > 1:
    print(f'A soma dos {counter} valores foi {sum}!')
else:
    print('Você não informou nenhum valor!')
