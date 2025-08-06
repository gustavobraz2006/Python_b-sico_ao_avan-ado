nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    
    nome_invertido = nome[-1:-1 - len(nome):-1]
    qnt_caracnome = len(nome)
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    espaços_nome = nome.count(' ')
    quantidade_letras = qnt_caracnome - espaços_nome

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    print(f'Seu nome tem essa quantidade de caractéres:{qnt_caracnome}')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
    print(f'Seu nome tem {espaços_nome} espaços')
    print(f'Seu nome tem {quantidade_letras} letras')

else:
    print('Você não digitou os campos corretamente')


    
    


          
                                 

