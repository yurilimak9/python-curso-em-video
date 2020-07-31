print('\033[1;34m=' * 21)
print('\033[1;36m{:^22}\033[m'.format('CORES NO TERMINAL'))
print('\033[1;34m=\033[m' * 21)

"""
style = {none: 0, bold: 1, underline: 4, negative: 7}
text = {branco: vázio, preto: 30, vermelho: 31, verde: 32, amarelo: 33, azul_01: 34, roxo: 35, azul_02: 36, cinza: 37}
back = {branco: vázio, preto: 40, vermelho: 41, verde: 42, amarelo: 43, azul_01: 44, roxo: 45, azul_02: 46, cinza: 47}
"""

name = 'Yuri'
cores = {
    'clean': '\033[m', 'verde': '\033[1;32m', 'azul': '\033[1;34m', 'amarelo': '\033[33m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['verde'], name,cores['clean']))

print('\033[0;;41m TEST \033[m')
print('\033[1;33;46m TEST \033[m')
print('\033[1;35;43m TEST \033[m')
print('\033[;;42m TEST \033[m')
print('\033[;37;40m TEST \033[m')
print('\033[;;40m TEST \033[m')
