# Desempacotamento em chamadas 
# de métodos e funções

string = 'ABCD'
lista = ['carlos, joelma, pedrinho']
tupla = 'python', 'é', 'top'

salas = [
    # 0        1         
    ['Maria', 'Helena', ],
    # 0
    ['Elaine'], #1
    # 0        1        2              3
    ['Luiz', 'Leticia', 'Fabrício', (0, 10, 20, 30)], # 2
]

print(*string) # Asterisco desempacota a string, A B C D
print(*lista) # Carlos, Joelma, Pedrinho
print(*tupla) # Python é top
print(*salas, sep='\n') # Desempacota a lista de listas e imprime cada lista em uma linha