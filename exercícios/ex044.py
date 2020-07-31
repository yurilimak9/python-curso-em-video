print('-' * 20)
print('{:^20}'.format('Exercício 044'))
print('-' * 20)

print('{:*^30}'.format(' PromoBlue '))

price_shopping = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')

option = int(input('Qual é a opção? '))

if option == 1:
    total = price_shopping - ((price_shopping * 10) / 100)
elif option == 2:
    total = price_shopping - ((price_shopping * 5) / 100)
elif option == 3:
    total = price_shopping
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(total / 2))
elif option == 4:
    total = price_shopping + ((price_shopping * 20) / 100)
    parcel = int(input('Em quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcel, (total / parcel)))
else:
    total = price_shopping
    print('\033[1;31mOpção inválida de pagamento. Tente novamente!\033[m')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(price_shopping, total))