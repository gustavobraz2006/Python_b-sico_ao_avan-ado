'''Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
methodo isdigit- checa se o usuário digitou apenas números obs: . não conta como número
'''
#se acontecer um erro no try ja pula direto pro except 
#semelhante a if else, entretanto evita alguns erros

numero_str = input('Digite um número que irei dobrá-lo: ')

try: 
    
    numero_float = float(numero_str)
    print(f'FLOAT : {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:

    print('Isso não é um número.')
