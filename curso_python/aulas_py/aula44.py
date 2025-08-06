''' For + Range 
range -> range(start, stop, step)
'''

numeros = range(0, 250, 8)

for numero in numeros:
    print(numero)
    

multiplos = len(numeros)

try:

    verificador = input('Digite o número que você deseja verificar se é múltiplo: ')
    verificador_int = int(verificador)
    if verificador_int in numeros:
        print(f'{verificador_int} é múltiplo de 8')

    else:
        print(f'{verificador_int} não é multiplo de 8')

except:

    print('Digite um número válido')

print(f'A quantidade de multiplos de 8 é {multiplos}')

   