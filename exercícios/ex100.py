from random import randint
from time import sleep
from operator import itemgetter

print('{:-^23}'.format(' Exercício 100 '))

players = dict()
for i in range(1, 5):
    players[f"jogador{i}"] = randint(1, 6)

print('Valores sorteados:')
for key, value in players.items():
    sleep(0.5)
    print(f'\tO {key} tirou {value}')

print('\nRanking dos jogadores:')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for index, player in enumerate(ranking):
    sleep(0.5)
    print(f'\t{index + 1}º lugar - {player[0]}: {player[1]}')
