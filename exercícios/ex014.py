print('=' * 20)
print('{:^20}'.format('Exercício 014'))
print('=' * 20)

temperature = float(input('Informe a temperatura em °C: '))

convert_fahrenheit = (temperature * 9 / 5) + 32

print(f'A temperatura de {temperature:.1f}°C corresponde a {convert_fahrenheit:.1f}°F!')