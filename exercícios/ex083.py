print('-' * 23)
print('{:-^23}'.format(' Exercício 083 '))
print('-' * 23)

expression = str(input('Digite a expressão: '))

stack = list()
for c in expression:
    if c == '(':
        stack.append('(')
    elif c == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if not stack:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
