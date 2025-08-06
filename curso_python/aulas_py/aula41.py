''' while / else'''

string = 'Valorqualquer'

i = 0

while i < len(string):

    letra = string[i]
    
    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('Não encontrei nenhum espaço na string.')

print('Fora do while.')


#while/else     após o término do laço do while, o else é executado
# o else só não é executado quando o programa possui algum break para finalizar o laço