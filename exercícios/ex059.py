from time import sleep

print('-' * 23)
print('{:+^23}'.format(' Exercício 059 '))
print('-' * 23)

first_value = int(input('Primeiro valor: '))
second_value = int(input('Segundo valor: '))

option = 0
while option != 5:
    print('+' * 30)
    print('[1] Somar. \n[2] Multiplicar. \n[3] Maior. \n[4] Novos números. \n[5] Sair do programa.')
    print('+' * 30)

    option = int(input('Qual é sua opção? '))

    if option == 1:
        print('A soma entre {} e {} é {}'.format(first_value, second_value, (first_value + second_value)))
        print('-' * 30)
    elif option == 2:
        print('O resultado de {} x {} é {}'.format(first_value, second_value, (first_value * second_value)))
        print('-' * 30)
    elif option == 3:
        print('Entre {} e {} o maior valor é {}'.format(first_value, second_value,
                                                        (first_value if first_value > second_value else second_value)))
        print('-' * 30)
    elif option == 4:
        first_value = int(input('Primeiro valor: '))
        second_value = int(input('Segundo valor: '))
    else:
        if option != 5:
            print('Opção inválida. Tente novamente!')
    sleep(3)

print('Finalizando...')
sleep(1)
print('-' * 30)
print('Fim do programa! Volte sempre!')
