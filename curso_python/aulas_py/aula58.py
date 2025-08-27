'''
split e join com list e str
split - divide uma string # str (list)
join - une uma string # str
strip - remove espaços em branco # str
capitalize - deixa a primeira letra maiúscula # str
'''

frase = '    O Brasil é o país do futebol, o Brasil é penta     '
lista_frases_cruas = frase.split(', ')
print(lista_frases_cruas) #['O Brasil é o país do futebol', 'o Brasil é penta.']
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases) #['O Brasil é o país do futebol', 'o Brasil é penta.']

letras_unidas = '-'.join('abc') 
print(letras_unidas) #a-b-c
frases_unidas = ' e '.join(lista_frases)
print(frases_unidas) #O Brasil é o país do futebol e o Brasil é penta.