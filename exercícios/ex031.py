print('-' * 20)
print('{:^20}'.format('Exercício 031'))
print('-' * 20)

distance = float(input('Qual a distância da sua viagem? '))

print('Você está prestes a começar um viagem de {:.0f}Km'.format(distance))
if distance <= 200:
    ticket_price = distance * 0.5
else:
    ticket_price = distance * 0.45

print('Preço da passagem: R${:.2f}'.format(ticket_price))
