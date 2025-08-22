'''Cuidados com dados mutáveis
= - copiado o valor(imutáveis)
= - aponta para o mesmo valor na memória(mutável)
'''
lista_a = ['Luiz', 'Maria']
#lista_b = lista_a
lista_b = lista_a.copy() #metodo que faz com que a lista b não se altere e cria outra lista

lista_a[0] = 'Qualquer coisa'
print(lista_b) # mesmo mudando a lista a , a lista b também é modificada por ser um valor mutável
print(lista_a)
