print('=' * 20)
print('{:^20}'.format('Exercício 009'))
print('=' * 20)

salary = float(input('Qual é o salário do Funcionário? R$'))

new_salary = salary + ((salary * 15) / 100)

print(f'Um funcionário que ganhava R${salary:.2f}, com 15% de aumento, passa a receber R${new_salary:.2f}')