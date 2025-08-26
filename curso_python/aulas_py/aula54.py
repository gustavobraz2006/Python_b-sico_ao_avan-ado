''' Introdução ao desempacotamento em Python '''

# Desempacotamento de listas/tuplas
lista = ['Luiz', 'João', 'Maria']
'''n1, n2, n3 = lista
print(n1, n2, n3)
print(n1)
print(n2)
print(n3)'''

_, nome, *_ = ['Luiz', 'João', 'Maria']
print(nome)

# Desempacotamento de strings
nome = 'Luiz Otávio'
n1, n2 = nome.split()
print(n1, n2)



