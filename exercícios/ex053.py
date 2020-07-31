print('-' * 23)
print('{:+^23}'.format(' Exercício 053 '))
print('-' * 23)

phrase = str(input('Digite uma frase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)

inverse = ''
for letter in range(len(together) - 1, -1, -1):
    inverse += together[letter]

if inverse == together:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
