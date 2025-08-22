''' Listas em Python 
Tipo list - mutável 
suporta varios valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2] #deleta o indice 2 , não vai aparecer mais o 300
#evitar mover muitos indices porque requer muito processamento
lista.append(50) # adiciona mais um indice e coloca o valor na frente
lista.pop() # apaga o ultimo item da lista, apagando o 50 que é o ultimo valor seguindo a ordem

lista.append(60)
lista.append(70)
print(lista)
print(lista[2])

ultimo_valor = lista.pop()
print(lista, 'Removido,' ,ultimo_valor)
