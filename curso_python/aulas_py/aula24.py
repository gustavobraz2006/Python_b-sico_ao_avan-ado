#operadores in e not in
# string são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1

#nome = 'Otávio'

#print(nome[2]) á
#print(nome[-4]) á

#print('á' in nome) True
#print('vio' in nome) True
#print('zero' in nome) False
#print('vio' not in nome) False
#print('zero' not in nome) True

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

