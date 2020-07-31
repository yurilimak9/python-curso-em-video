print('-' * 20)
print('{:^20}'.format('Exercício 026'))
print('-' * 20)

frase = str(input('Digite uma frase: ')).upper().strip()

print('Quantes vezes apararece a letra "a" na frase? {}'.format(frase.count('A')))
print('Em que posição aparece a letra "a" pela primeira vez na frase? {}'.format(frase.find('A') + 1))
print('Em que posição aparece a letra "a" pela última vez na frase? {}'.format(frase.rfind('A') + 1))
