print('=' * 20)
print('{:^20}'.format('Exercício 015'))
print('=' * 20)

rented_days = int(input('Quantos dias alugados? '))
travelled_distance = float(input('Quantos Km rodados? '))

amount_payable = (rented_days * 60) + (travelled_distance * 0.15)

print(f'O total a pagar é de R${amount_payable:.2f}')