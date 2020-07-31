from random import randint
from time import sleep

print('-' * 20)
print('{:^20}'.format('Exercício 045'))
print('-' * 20)

itens = ('Pedra', 'Papel', 'Tesoura')

print('''
Suas opções:
[ 0 ] PEDRA.
[ 1 ] PAPEL.
[ 2 ] TESOURA.''')

pc = randint(0, 2)
player = int(input('Qual é sua jogada? '))

if player in [0, 1, 2]:
    sleep(0.6)
    print('\033[1;33m{:>10}\033[m'.format('JO'))
    sleep(0.6)
    print('\033[1;32m{:>10}\033[m'.format('KEN'))
    sleep(0.6)
    print('\033[1;36m{:>10}\033[m'.format('PO!!!'))
    sleep(0.6)

    print('*' * 25)
    print('Computador jogou {} \nJogador jogou {}'.format(itens[pc], itens[player]))
    print('*' * 25)

    if player == pc:
        print('\033[1;33m{:^25}\033[m'.format('EMPATE!'))
    elif player == 0 and pc == 2:
        print('\033[1;32m{:^25}\033[m'.format('JOGADOR VENCEU!'))
    elif player == 1 and pc == 0:
        print('\033[1;32m{:^25}\033[m'.format('JOGADOR VENCEU!'))
    elif player == 2 and pc == 1:
        print('\033[1;32m{:^25}\033[m'.format('JOGADOR VENCEU!'))
    else:
        print('\033[1;36m{:^25}\033[m'.format('COMPUTADOR VENCEU!'))
else:
    print('\033[1;31mOpção inválida. Tente novamente!\033[m')
