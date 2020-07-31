print('-' * 20)
print('{:^20}'.format('Exercício 043'))
print('-' * 20)

peso = float(input('Qual é seu peso? (Kg) '))
height = float(input('Qual é sua altura? (m) '))

imc = peso / pow(height, 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL!')
elif imc < 30:
    print('Você está em SOBREPESO!')
elif imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
