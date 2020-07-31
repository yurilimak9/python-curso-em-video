print('-' * 23)
print('{:+^23}'.format(' Exercício 050 '))
print('-' * 23)

sum = 0
for i in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        sum += num

print("A soma dos valores PARES foi {}".format(sum))
