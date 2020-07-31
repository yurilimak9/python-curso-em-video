print('=' * 20)
print('{:^20}'.format('AULA 15'))
print('=' * 20)

counter = sum = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break

    sum += num
    counter += 1

print(f'Você informou {counter} números.')
print(f'E a soma dos valores informados foi de {sum}.')
