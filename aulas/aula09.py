print('-' * 20)
print('{:^20}'.format('AULA 09'))
print('-' * 20)

frase = 'Curso em Vídeo Python'
print("Frase 01: {}".format(frase))
print('Comprimento: {}'.format(len(frase)))
print('Quatas vezes aparece a letra "o"? {}'.format(frase.count('o')))
print('Em que posição inicio "deo"? {}'.format(frase.find('deo')))
print('Existe a palavra "Curso" na frase? {}'.format("Curso" in frase))

print('+' * 30)
frase02 = '   Aprenda Python '
print('Frase 02: {}'.format(frase02))
print('Frase com espaços no inicio e fim removidos: {}'.format(frase02.strip()))
