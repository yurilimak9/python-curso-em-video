print('+ {:=^23} +'.format(' AULA 19 '))

locadora = list()
filme = dict()
while True:
    filme['titulo'] = str(input('Titulo: ')).strip().title()
    filme['ano'] = int(input('Ano: '))
    filme['diretor'] = str(input('Diretor: ')).strip().title()
    locadora.append(filme.copy())

    while True:
        option = str(input('Quer continuar? ')).strip().upper()[0]
        if option in 'SN':
            break
        print('Opção inválida, tente novamente!')
    if option == 'N':
        break


print('{:=^23}'.format(' FILMES '))
for filme in locadora:
    print(f'Titulo: {filme["titulo"]}')
    print(f'Ano: {filme["ano"]}')
    print(f'Diretor: {filme["diretor"]}')
    print('-' * 23)
