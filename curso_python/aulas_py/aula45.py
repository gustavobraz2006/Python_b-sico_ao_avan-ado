'''
Iterável  -> str, range, etc (__iter__)
Iterador  -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor 
iter -> me entregue seu iterador
'''

''' Explicando o funcionamento do for in'''

#for letra in texto:
    #print(letra)


texto = 'Jorge Amado'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    
    except StopIteration:
        break

