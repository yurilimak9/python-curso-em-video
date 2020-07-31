print('-' * 20)
print('{:^20}'.format('Exercício 036'))
print('-' * 20)

house_value = float(input('Qual o valor da casa? R$'))
salary = float(input('Qual o seu salário mensal? R$'))
deadline = int(input('Em quantos anos deseja pagar a casa? '))

monthly_installment = house_value / (deadline * 12)
wage_percentage = (salary * 30) / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(house_value, deadline, monthly_installment))
if wage_percentage <= monthly_installment:
    print('Emprétismo Negado!')
else:
    print('Empréstimo Aprovado!')
