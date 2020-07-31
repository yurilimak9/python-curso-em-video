print('-' * 20)
print('{:^20}'.format('Exercício 023'))
print('-' * 20)

num = int(input('Digite um número entre 0 e 9999: '))

unity = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(unity))
print('Dezena: {}'.format(ten))
print('Centena: {}'.format(hundred))
print('Milhar: {}'.format(thousand))
