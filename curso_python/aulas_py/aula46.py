# O que aprendemos no while também funciona no for (continue, break, else ...)

for i in range(10):

    if i == 2:
        print('Seu i é = 2 , pulando...')
        continue
        
    if i == 8:
        print('i = 8 , seu else não executára')

    for j in range(1, 3, 1):
        print(i, j)

else:
    print('For completo com sucesso.')