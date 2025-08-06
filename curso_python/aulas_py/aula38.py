'''
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdade
Loop infinito-> quando um código não tem fim
'''
#while dentro de while

qtd_Linhas = 5
qtd_colunas = 5
linha = 1

while linha <= qtd_Linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou') 
