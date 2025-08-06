'''
Calculadora com while
+ - / * 

'''



while True:
    try:
        sair = input('Você quer sair do programa? [s]im: ')
        sair = sair.lower()
        sair = sair.startswith('s')

        if sair:
            break

        primeiro_numero = input('Digite o primeiro número da operação: ')
        primeiro_numero_float = float(primeiro_numero)

        segundo_numero = input('Digite o segundo número da operação: ')
        segundo_numero_float = float(segundo_numero)

        operacao = input('Digite a operação que você deseja fazer: \n1.Adição\n2.Subtração\n3.Divisão\n4.Multiplicação\n Escolha(1-4): ')

        if operacao == '1':
            resultado_adicao =  primeiro_numero_float + segundo_numero_float 
            print(f'o resultado é {resultado_adicao}')

        elif operacao == '2':
            resultado_subtracao = primeiro_numero_float - segundo_numero_float
            print(f'o resultado é {resultado_subtracao}')

        elif operacao == '3':
            if segundo_numero_float == 0:
                print('Divisão impossível')
                continue
            resultado_divisao = primeiro_numero_float / segundo_numero_float
            print(f'o resultado é {resultado_divisao}')

        elif operacao == '4':
            resultado_multiplicacao = primeiro_numero_float * segundo_numero_float
            print(f'o resultado é {resultado_multiplicacao}')

        else:
            print('Operação inválida, tente novamente.')

    except ValueError:
        print('Digite apenas números.')
        
        