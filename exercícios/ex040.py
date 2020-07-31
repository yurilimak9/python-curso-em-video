print('-' * 20)
print('{:^20}'.format('Exercício 040'))
print('-' * 20)

first_note = float(input('Primeira nota: '))
second_note = float(input('Segunda nota: '))

mean = (first_note + second_note) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(first_note, second_note, mean))
if mean < 5:
    print('O aluno está REPROVADO!')
elif 7 > mean >= 5:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
