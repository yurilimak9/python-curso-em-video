print('-' * 23)
print('{:-^23}'.format(' Exercício 067 '))
print('-' * 23)

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break

    for i in range(0, 11):
        result = num * i
        print(f'{num} x {i:>2} = {result}')

print('PROGRAMA TABUADA ENCERRADO. \nVolte sempre!')
