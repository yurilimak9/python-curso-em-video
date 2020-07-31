from time import sleep

print('{:-^23}'.format(' Exercício 089 '))

pupils = list()
while True:
    name = str(input('Nome: ')).strip().title()
    first_note = float(input('Nota 01: '))
    second_note = float(input('Nota 02: '))
    mean = (first_note + second_note) / 2

    pupils.append([name, [first_note, second_note], mean])
    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if option in 'SN':
            break
    if option == 'N':
        break

print('-' * 23)
print('{:<4}{:<10}{}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 23)
for index, pupil in enumerate(pupils):
    print('{:<4}{:<10}{:>5.1f}'.format(index, pupil[0], pupil[2]))
print('-' * 23)

while True:
    while True:
        pupil = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
        if pupil == 999 or pupil < len(pupils):
            break
        print('Aluno não encontrado, tente novamente!')
    if pupil == 999:
        break

    print('Notas de {} são {}'.format(pupils[pupil][0], pupils[pupil][1]))
    print('~' * 46)

print('*' * 46)
print('Finalizando...')
sleep(0.5)
print('{:*^46}'.format(' VOLTE SEMPRE '))
