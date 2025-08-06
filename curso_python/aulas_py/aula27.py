'''Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
p : passos, normalmente de 1 em 1 mas posso mudar
obs.:a função len retorna a qtd
de caracteres da str
'''
#contagem de índices começa do 0
variavel = 'Olá mundo'
print(variavel[4:8]) #retorna mund
print(variavel[4:])  #retorna mundo
print(len(variavel[3:5])) #conta a qntde de caracteres OBS: o espaço vazio também conta
print(variavel[0:len(variavel):2])#retorna Oámno
print(variavel[-1:-10:-1])#retorna o inverso


