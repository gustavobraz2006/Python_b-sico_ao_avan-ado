'''enummerate - enumera iteráveis (índices)'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista.append('Eduardo')

for indice, nome in enumerate(lista):
      print(indice, nome)

# OBS: A função enumerate retorna um objeto enumerate que é um iterável
# que gera tuplas com (índice, valor) para cada valor no iterável passado

# for nome in lista:
#     print(nome)
#     print(lista.index(nome), nome)
#     # OBS: Não usar o método index em listas que possuem valores repetidos, pois ele retorna o índice do primeiro valor
#     # Exemplo:
#     # lista = ['Maria', 'Helena', 'Luiz', 'Maria']
#     # Maria 0
#     # Helena 1
#     # Luiz 2
#     # Maria 0 <- retornou o índice do primeiro valor

for indice in range(len(lista)):
    print(indice, lista[indice])
# OBS: Não é a forma ideal de fazer, mas funciona
