print('-' * 23)
print('{:-^23}'.format(' Exercício 081 '))
print('-' * 23)

values = list()
while True:
    num = int(input('Digite um valor: '))
    values.append(num)

    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if option in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!')
    if option == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(values)} elementos.')
values.sort(reverse=True)
print(f'Os valores em ordem decrescente são {values}')
if 5 in values:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
