print('-' * 23)
print('{:-^23}'.format(' Exercício 073 '))
print('-' * 23)

times = ('Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG',
         'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza',
         'Goiás', 'Sport', 'Vasco')

print('+-' * 140)
print(f'Lista de times do Brasileirão: {times}')
print('+-' * 140)
print(f'Os 5 primeiros são: {times[:5]}')
print('+-' * 140)
print(f'Os 4 últimos são: {times[-4:]}')
print('+-' * 140)
print(f'Times em ordem alfabética: {sorted(times)}')
print('+-' * 140)
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição')

