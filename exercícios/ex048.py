print('-' * 23)
print('{:+^23}'.format(' Exercício 048 '))
print('-' * 23)

sum = 0
quantity = 0
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        sum += i
        quantity += 1

print('A soma de todos os {} valores solicitados é {}'.format(quantity, sum))
