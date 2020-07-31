print('=' * 21)
print('{:^21}'.format('AULA 17'))
print('=' * 21)

lanches = ['hamburguer', 'suco', 'pizza', 'pudim']
# adiciona um elemento no final da lista
lanches.append('café')
lanches.append('picolé')

# remover um elemento se ele existir
if 'suco' in lanches:
    lanches.remove('suco')

# ordena valores do maior para o menor
lanches.sort(reverse=True)

# insere um valor na posição que desejar
lanches.insert(0, 'cachorro quente')

# remove o último elemento se não especificado um índice
lanches.pop()

# tamanho da lista
size = len(lanches)

for index, lanche in enumerate(lanches):
    print(f'[{index}] {lanche.title()}')
print(f'Tamanho da lista: {size}')

# cria uma lista preenchida com os vaores de 4 a 10
values = list(range(4, 11))
print(values)

