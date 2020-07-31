from math import sin, cos, tan, radians

print('=' * 20)
print('{:^20}'.format('Exercício 018'))
print('=' * 20)

a = float(input('Digite o ângulo que você deseja: '))

# Conversão para radianos
angle = radians(a)

sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)

print(f'Informações referentes ao ângulo {a:.1f}°: \nSeno = {sine:.2f} \nCosseno = {cosine:.2f} \nTangente = {tangent:.2f}')
