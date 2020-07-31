print('=' * 20)
print('{:^20}'.format('Exercício 011'))
print('=' * 20)

width = float(input('Qual a largura da parede? '))
height = float(input('Qual a altura da parede? '))

area = width * height
required_ink = area / 2

print(f'Sua parede tem a dimensão de {width}x{height} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {required_ink:.2f}L de tinta')