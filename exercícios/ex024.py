print('-' * 20)
print('{:^20}'.format('Exercício 024'))
print('-' * 20)

city = str(input('Digite o nome de uma cidade: '))

print('A cidade {} começa com o nome "Santo"? {}'.format(city.title().strip(), city.upper().split()[0] == 'SANTO'))