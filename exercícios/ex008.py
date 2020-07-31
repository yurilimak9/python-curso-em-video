print('=' * 20)
print('{:^20}'.format('Exercício 008'))
print('=' * 20)

measure = float(input('Digite um valor em metros: '))

km = measure / 1000
hm = measure / 100
dam = measure / 10
dm = measure * 10
cm = measure * 100
mm = measure * 1000

print(f'Conversor de medidas:')
print(f'{measure}m corresponde a {km}km')
print(f'{measure}m corresponde a {hm}hm')
print(f'{measure}m corresponde a {dam}dam')
print(f'{measure}m corresponde a {dm}dm')
print(f'{measure}m corresponde a {cm}cm')
print(f'{measure}m corresponde a {mm}mm')