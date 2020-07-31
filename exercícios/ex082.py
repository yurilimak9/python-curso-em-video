print('-' * 23)
print('{:-^23}'.format(' Exercício 082 '))
print('-' * 23)

values = list()
list_odd = list()
list_even = list()
while True:
    num = int(input('Digite um número: '))
    values.append(num)

    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)

    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if option in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!')
    if option == 'N':
        break


print('-=' * 30)
print(f'A lista completa é {values}')
print(f'A lista de pares é {list_even}')
print(f'A lista de ímpares é {list_odd}')
