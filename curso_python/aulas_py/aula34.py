'''
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdade
Loop infinito-> quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break