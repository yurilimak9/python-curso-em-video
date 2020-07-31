print('-' * 23)
print('{:-^23}'.format(' Exercício 071 '))
print('-' * 23)

print('*' * 30)
print('{:^30}'.format('BANCO K9'))
print('*' * 30)

value = int(input('Que valor quer sacar? R$'))
total = value
ballot = 100
total_ballot = 0
while True:
    if total >= ballot:
        total -= ballot
        total_ballot += 1
    else:
        if total_ballot > 0:
            print(f'Total de {total_ballot} cédulas de R${ballot}')

        if ballot == 100:
            ballot = 50
        elif ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 5
        elif ballot == 5:
            ballot = 1


        total_ballot = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO K9! \nTenha um bom dia!')
