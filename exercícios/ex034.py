print('-' * 20)
print('{:^20}'.format('Exercício 034'))
print('-' * 20)

salary = float(input('Qual é o salário do funcionário? R$'))

if salary <= 1250:
    new_salary = salary + (salary * 15) / 100
else:
    new_salary = salary + (salary * 10) / 100

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salary, new_salary))
