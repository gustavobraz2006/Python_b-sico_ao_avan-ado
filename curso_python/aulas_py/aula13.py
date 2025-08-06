nome ='Gustavo Braz'
altura = 1.82
peso = 79.5

imc = peso / (altura ** 2)
print(nome, 'tem', altura, 'de altura e', peso, 'kg de peso.')
print('O IMC de', nome, 'é', imc)     

#formatação de string
#f-strings
#f-strings são strings formatadas que permitem incluir expressões dentro de chaves {}
print(f'{nome} tem {altura} de altura e {peso} kg de peso.')
print(f'O IMC de {nome} é {imc}')


