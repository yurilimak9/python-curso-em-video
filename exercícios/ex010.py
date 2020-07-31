print('=' * 20)
print('{:^20}'.format('Exercício 010'))
print('=' * 20)

money = float(input('Quanto dinheiro você tem na carteira? R$'))

usd = money / 5.31

print(f'Com R${money:.2f} você pode comprar US${usd:.2f}')