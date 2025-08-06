nome_usuario = input('Digite seu primeiro nome: ')

if nome_usuario <= nome_usuario[0:4:1]:
    print('Seu nome é curto')

elif nome_usuario > nome_usuario[0:4:1] and nome_usuario <= nome_usuario[0:6:1]:
    print('Seu nome é normal')

elif nome_usuario > nome_usuario[0:6:1]:
    print('Seu nome é grande')

else:
    print('Digite seu nome corretamente')
