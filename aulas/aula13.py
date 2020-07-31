print('=' * 20)
print('{:^20}'.format('AULA 13'))
print('=' * 20)

sum_par = 0
sum_impar = 0
for i in range(1, 10):
    if i % 2 == 0:
        sum_par += i
    else:
        sum_impar += i

print(f'Soma dos pares é igual a {sum_par} e soma dos ímpares é igual a {sum_impar}')
