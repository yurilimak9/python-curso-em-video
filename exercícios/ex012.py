print('=' * 20)
print('{:^20}'.format('Exercício 009'))
print('=' * 20)

price = float(input('Qual é o preço do produto? R$'))

discount_price = price - ((price * 5) / 100)

print(f'O produto que custava R${price:.2f}, na promoção com desconto de 5% vai custar R${discount_price:.2f}')