print('{:-^23}'.format(' Exercício 090 '))

student = dict()

student['name'] = str(input('Nome: ')).strip().title()
student['mean'] = float(input(f'Média de {student["name"]}: '))
if student['mean'] < 5:
    student['situation'] = 'Reprovado'
elif student['mean'] < 7:
    student['situation'] = 'Recuperação'
else:
    student['situation'] = 'Aprovado'

print('-' * 23)
print('{:+^23}'.format(' STATUS '))
print('-' * 23)
for k, v in student.items():
    print(f'{k}: {v}')
