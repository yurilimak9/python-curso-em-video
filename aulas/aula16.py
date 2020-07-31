print('=' * 20)
print('{:^20}'.format('AULA 16'))
print('=' * 20)

lanches = ('hamburguer', 'suco', 'pizza', 'pudim')

print('{:-^20}'.format(' OPÇÕES '))

for index, lanche in enumerate(lanches):
    print(f'[{index + 1}] {lanche.title()}')

print('{:-^20}'.format(' Ordenado '))
for index, lanche in enumerate(sorted(lanches)):
    print(f'[{index + 1}] {lanche.title()}')
