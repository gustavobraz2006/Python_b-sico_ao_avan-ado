'''lista de listas e seus indices'''

salas = [
    # 0        1         
    ['Maria', 'Helena', ],
    # 0
    ['Elaine'], #1
    # 0        1        2              3
    ['Luiz', 'Leticia', 'Fabrício', (0, 10, 20, 30)], # 2
]

#print(salas[0][1]) # Helena
#print(salas[1][0]) # Elaine
#print(salas[2][3]) # (0, 10, 20, 30)
#print(salas[2][3][2]) # 20

for sala in salas:
    for item in sala:
        print(item)
        for i in item:
            print('->', i)
            