from random import randint
from time import sleep

print('-' * 20)
print('{:^20}'.format('Exercício 028'))
print('-' * 20)

numPC = randint(0, 5)
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)

player = int(input('Em qual número o computador esta pensando? '))

print('PROCESSANDO...')
sleep(2)

if numPC == player:
    print('VOCÊ GANHOU! O computador também pensou no número {}.'.format(player))
else:
    print('VOCÊ PERDEU! O computador pensou no número {} e você no {}.'.format(numPC, player))

