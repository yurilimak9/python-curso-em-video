print('-' * 23)
print('{:-^23}'.format(' Exercício 079 '))
print('-' * 23)

values = list()
while True:
    num = int(input('Digite um valor: '))
    if num in values:
        print('Valor duplicado! Não vou adicionar...')
    else:
        values.append(num)
        print('Valor adicionado com sucesso...')

    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if option in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!')
    if option == 'N':
        break

print(f'Você digitou os valores {sorted(values)}')
