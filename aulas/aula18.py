print('=' * 21)
print('{:^21}'.format('AULA 18'))
print('=' * 21)

people = list()
data = list()
for i in range(3):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idade: ')))
    people.append(data.copy())
    data.clear()

print(people)
