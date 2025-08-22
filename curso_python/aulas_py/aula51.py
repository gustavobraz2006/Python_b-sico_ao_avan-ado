''' Listas em Python 
Tipo list - mutável 
suporta varios valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
 append - Adiciona um item ao final 
 insert - Adiciona um item no índice escolhido
 pop - Remove do final ou do índice escolhido
 del - apaga um índice
 clear - limpa a lista
 extend - estende a lista
   + - concatena listas
Create Read Update Delete
criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c) #concatena as listas 
lista_a.extend(lista_b)
print(lista_a) #extend é um método que retorna no objeto lista_a
#extend retorna None então é uma ação que o objeto deve executar 