print('-' * 20)
print('{:^20}'.format('Exercício 037'))
print('-' * 20)

num = int(input('Digite um número inteiro: '))

print('''
Escolha uma opção abaixo:
[ 1 ] Para Binário.
[ 2 ] Para Octal.
[ 3 ] Para Hexadecimal.''')

option = int(input('Sua opção: '))

if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')