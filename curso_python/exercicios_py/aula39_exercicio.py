'''
iterando strings com while '''
#       123456789101112
nome = 'Gustavo Braz'
#  13121110987654321

tamanho_nome = len(nome)
indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)

   
