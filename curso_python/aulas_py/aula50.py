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

lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]

#lista.clear()  apaga a lista toda

lista.insert(0, 6) #considera o primeiro valor como indice e outro insere
print(lista)