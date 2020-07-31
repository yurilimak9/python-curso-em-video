from random import randint

print('-' * 23)
print('{:+^23}'.format(' Exercício 058 '))
print('-' * 23)

print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

pc = randint(0, 10)

attempts = 0
hit = False
while not hit:
    player = int(input('Qual é seu palpite? '))
    attempts += 1
    if player != pc:
        if player > pc:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
    else:
        hit = True

print('Acertou com {} tentativas. Parabéns!'.format(attempts))
