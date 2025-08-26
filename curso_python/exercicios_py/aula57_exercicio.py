#exercicio lista de compras

lista = []
print('FAÇA SUA LISTA DE COMPRAS!!')
while True:
    resposta = input('[i]nserir  [a]pagar  [l]istar ').lower().strip()[0]

    if resposta == 'i':
        produto = input('Digite o nome do produto: ').strip()
        lista.append(produto)
        print(f'{produto} adicionado à lista.')
        for indice, produto in enumerate(lista):
            print(indice, produto)
            
    elif resposta == 'a':
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
        for indice, produto in enumerate(lista):
            print(indice, produto)

    else:
        print('Digite valores válidos.')
