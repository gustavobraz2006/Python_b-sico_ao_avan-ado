#exercicio lista de compras
import os

lista = []
print('FAÇA SUA LISTA DE COMPRAS!!')
while True:
    resposta = input('[i]nserir  [a]pagar  [l]istar ').lower().strip()[0]

    if resposta == 'i':
        os.system('cls')
        produto = input('Digite o nome do produto: ').strip()
        lista.append(produto)
        print(f'{produto} adicionado à lista.')
        for indice, produto in enumerate(lista):
            print(indice, produto)
            
    elif resposta == 'a':
        os.system('cls')
        apagarproduto = input('Digite o indice do produto que queira apagar: ').strip()
        if not apagarproduto.isdigit():
            print('Digite um índice válido.')
            continue
        if int(apagarproduto) >= len(lista):
            print('Índice não encontrado na lista.')
            continue
        lista.pop(int(apagarproduto))
        print('Produto removido com sucesso.')
        for indice, produto in enumerate(lista):
            print(indice, produto)

    elif resposta == 'l':
        os.system('cls')
        for indice, produto in enumerate(lista):
            print(indice, produto)

    else:
        print('Digite valores válidos.')
    continuar = input('Deseja continuar? [s]im ou [n]ão ').lower().strip()[0]
    if continuar == 'n':
        break   
print('Obrigado por usar nossa lista de compras!')  