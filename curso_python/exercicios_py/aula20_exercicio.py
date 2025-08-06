primeiro_valor = input('Digite o primeiro número: ')
segundo_valor = input('Digite o segundo número: ')

flprimeiro_valor = float(primeiro_valor)
flsegundo_valor = float(segundo_valor)

if flprimeiro_valor > flsegundo_valor:
    print(f'O primeiro valor "{primeiro_valor}" é maior que o segundo valor "{segundo_valor}"')

elif flprimeiro_valor < flsegundo_valor:
    print(f'O segundo valor "{segundo_valor}" é maior que o primeiro valor "{primeiro_valor}"')

else:
    print('Digite os valores corretamente')
    
