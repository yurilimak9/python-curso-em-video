print('-' * 23)
print('{:-^23}'.format(' Exercício 077 '))
print('-' * 23)

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
    print(f'\nNa palavra {word.upper()} temos:', end=' ')
    for letra in word:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
