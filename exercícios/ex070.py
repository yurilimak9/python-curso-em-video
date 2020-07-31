print('-' * 23)
print('{:-^23}'.format(' Exercício 070 '))
print('-' * 23)

print('*' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('*' * 30)

cheaper_name = ''
total = over_a_thousand = cheaper_price = counter = 0
while True:
    product_name = str(input('Nome do produto: ')).strip().title()
    price = float(input('Preço: R$'))

    total += price
    if price > 1000:
        over_a_thousand += 1

    if counter == 0:
        cheaper_name = product_name
        cheaper_price = price
    else:
        if price < cheaper_price:
            cheaper_price = price
            cheaper_name = product_name
    counter += 1

    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if option in 'SN':
            break
        print('Opção inválida. Tente novamente!')

    if option == 'N':
        break

print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')

if over_a_thousand == 1:
    print(f'Temos {over_a_thousand} produto custando mais de R$1000.00')
elif over_a_thousand > 1:
    print(f'Temos {over_a_thousand} produtos custando mais de R$1000.00')
else:
    print(f'Não temos nenhum produto custando mais de R$1000.00')

print(f'O produto mais barato foi: {cheaper_name} - R${cheaper_price}')