from random import randint
from time import sleep

print('-' * 23)
print('{:-^23}'.format(' Exercício 088 '))
print('-' * 23)

print('{:^23}'.format('JOGA NA MEGA SENA'))
print('-' * 23)

quantity = int(input('Quantos jogos você quer que eu sorteie? '))

numbers = list()
for i in range(1, quantity + 1):
    for j in range(6):
        while True:
            value = randint(1, 60)
            if value not in numbers:
                numbers.append(value)
                break

    print(f'Jogo {i}: {sorted(numbers)}')
    sleep(0.5)
    numbers.clear()
