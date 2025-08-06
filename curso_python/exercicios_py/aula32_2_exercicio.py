hora_usuario = input('Digite o valor das horas inteiras de agora: ')

try:
    hora_usuario_int = int(hora_usuario)

    if hora_usuario_int >= 0 and hora_usuario_int <= 11:

        print('Bom dia!')

    elif hora_usuario_int >= 12 and hora_usuario_int <= 17:

        print('Boa tarde!')

    elif hora_usuario_int >= 18 and hora_usuario_int <= 23:
        
        print('Boa noite!')

    else:

        print('Hora inválida')

except ValueError:
    print('Digite o valor das horas inteiras por favor.')

    


