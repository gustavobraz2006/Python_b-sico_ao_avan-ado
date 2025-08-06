

#somente para valores positivos
 
'''numero_str = input('Digite um número inteiro: ')

if numero_str.isdigit():

    numero_inteiro = float(numero_str)
    numero_par = numero_inteiro % 2 == 0
    
    if numero_par:
        print('Seu número é par')

    else:
        print('Seu número é impar')


else:
    print('Digite um número inteiro corretamente')'''


numero_str = input('Digite um número inteiro: ')

try:

    numero_int = int(numero_str)
    numero_par = numero_int % 2 == 0
    
    if numero_par:
        print(f'Seu número {numero_int} é par')

    else:
        print('Seu número {numero_int} é impar')

except ValueError:
    
    print('Digite um número inteiro corretamente')













