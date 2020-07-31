print('-' * 23)
print('{:-^23}'.format(' Exercício 085 '))
print('-' * 23)

odd = list()
even = list()
values = [even, odd]
for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)



print('-' * 60)
print(f'Os valores pares digitados foram: {sorted(even)}')
print(f'Os valores ímpares digitados foram: {sorted(odd)}')
