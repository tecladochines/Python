from b_enun54_exerc import odd_even, hour_day, name_len #importação dos métodos criados no exercício

while True: #laço para repetir o menu toda vez que um método for encerrado e quando não é digitado uma das opções.
    print('\n' + '='*30)
    print(' '*8 + 'MENU PRINCIPAL')
    print('='*30)
    print('1. Par/Impar')
    print('2. Horas')
    print('3. Nome')
    print('0. Sair')
    print('='*30)

    try: #try except para tratar quando não for digitado um número.
        print('-'*30)
        menu_input = input('Digite o número de número referente a sua opção: ') #input do user
        print('-'*30)
        int_menu_input = int(menu_input) #conversão do input para int

        #condicionais para os métodos criados (importados de 'b_enun54_exerc')
        if int_menu_input == 1: odd_even()
        elif int_menu_input == 2: hour_day()
        elif int_menu_input == 3: name_len()
        elif int_menu_input == 0:
            print('-'*30)
            print('Programa encerrado!')
            print('-'*30)
            break
        else:
            print('-'*30)
            print('Digite uma opção válida!')
            print('-'*30)

    except ValueError as e:
        print('-'*30)
        print(f'>>>>>>Digite um número inteiro. ERROR: {e}')
        print('-'*30)
        




