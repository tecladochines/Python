"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def odd_even():
    while True: #laço para caso não seja digitado um int
        try: 
            print('-'*30)
            input_user = input('Digite um número inteiro: ') #input para digitar o número
            print('-'*30)
            int_input_user = int(input_user) #conversão do input para int

            if int_input_user % 2 == 0: #condicional para tratar os pares e impares
                print('-'*30)
                print('Número par!')
                print('-'*30)
                break

            elif int_input_user % 2 != 0:
                print('-'*30)
                print('Número ímpar!')
                print('-'*30)
                break

        except ValueError as e: #exceção para inputs não inteiros
            print('-'*30)
            print(f'>>>>>>Não foi digitado um número inteiro. Erro: {e}')
            print('-'*30)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
def hour_day():
    while True: #laço para repetir o input caso não seja inserido um número inteiro
        try:
            print('-'*30)
            input_user = input('Digite as horas (entre 1 e 23): ') # input user
            print('-'*30)
            int_input_user = int(input_user) #conversão do input para int

            #condiconais para tratar os inputs entre 0 e 23, fora isso cai no else.
            if int_input_user >= 0 and int_input_user <= 11: 
                print('-'*30)
                print('Bom dia')
                print('-'*30)
                break

            elif int_input_user >= 12 and int_input_user <= 17:
                print('-'*30)
                print('Boa tarde')
                print('-'*30)
                break

            elif int_input_user >= 18 and int_input_user <= 23:
                print('-'*30)
                print('Boa noite')
                print('-'*30)
                break

            else:
                print('-'*30)
                print('Digite um horário com números inteiros positivos')
                print('-'*30)

        except ValueError as e: # exceção para caso não seja digitado um número inteiro.
            print('-'*30)
            print(f'>>>>>>Não digitou um número inteiro. Erro: {e}')
            print('-'*30)

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
def name_len():
        print('-'*30)
        input_user = input('Digite seu nome: ') #input do usuário
        print('-'*30)

        #condicionais para implementar diferentes respostas ao usuário
        if len(input_user) > 0 and len(input_user) <= 4:
            print('-'*30)
            print('seu nome é curto.')
            print('-'*30)

        elif len(input_user) >= 5 and len(input_user) <= 6:
            print('-'*30)
            print('seu nome é normal.')
            print('-'*30)

        elif len(input_user) > 6:
            print('-'*30)
            print('seu nome é muito grande.')
            print('-'*30)