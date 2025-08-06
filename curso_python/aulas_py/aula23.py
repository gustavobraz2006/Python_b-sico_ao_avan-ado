#operador lógico "not"
# usado para inverter expressões
# not true = false
#  not false = true

senha = input('Digite sua senha: ')

if not senha:
    print('Você não digitou a senha.')


print(not True) #False
print(not False) #true