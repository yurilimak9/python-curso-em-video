print('-' * 20)
print('{:^20}'.format('Exercício 029'))
print('-' * 20)

car_speed = float(input('Qual a velocidade atual do carro? '))

allowed_speed = 80    # limite de velocidade
traffic_ticket_value = 7    # R$7,00 p/ cada Km acima do limite

if car_speed > allowed_speed:
    fine_amount = (car_speed - allowed_speed) * traffic_ticket_value
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${:.2f}!'.format(fine_amount))

print('Tenha um bom dia! Dirija com segurança!')

