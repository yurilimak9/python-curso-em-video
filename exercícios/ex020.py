from random import shuffle

print('=' * 20)
print('{:^20}'.format('Exercício 020'))
print('=' * 20)

pupil01 = str(input('Digite o nome do primeiro aluno: '))
pupil02 = str(input('Digite o nome do segundo aluno: '))
pupil03 = str(input('Digite o nome do terceiro aluno: '))
pupil04 = str(input('Digite o nome do quarto aluno: '))

pupils = [pupil01, pupil02, pupil03, pupil04]
shuffle(pupils)
print('Ordem de apresentação:')
print(pupils)
