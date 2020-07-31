from random import randint

print('-' * 23)
print('{:-^23}'.format(' Exercício 068 '))
print('-' * 23)

print('*' * 30)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('*' * 30)

winning = 0
while True:
    num = int(input('Diga um número: '))

    option = ' '
    while option not in 'PIÍ':
        option = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    pc = randint(0, 10)
    total = num + pc

    print('-' * 51)
    if total % 2 == 0:
        print(f'Você jogou {num} e o computador {pc}. Total de {total} DEU PAR')
        if option == 'P':
            print('VOCÊ GANHOU!')
            winning += 1
        else:
            break
    else:
        print(f'Você jogou {num} e o computador {pc}. Total de {total} DEU ÍMPAR')
        if option == 'I':
            print('VOCÊ GANHOU!')
            winning += 1
        else:
            break
    print('-' * 51)

    print('Vamos jogar novamente...')

print('VOCÊ PERDEU!')
if winning == 1:
    print(f'GAME OVER! Você venceu {winning} vez.')
elif winning > 1:
    print(f'GAME OVER! Você venceu {winning} vezes.')
else:
    print(f'GAME OVER! Você não venceu nenhuma vez.')
