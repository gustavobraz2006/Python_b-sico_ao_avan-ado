"""
Imprecisão de ponto flutuante
double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/3/tutorial/floatingpoint.html"""
#round função que arredonda o valor flutuante
#import decimal 
#utilizando a biblioteca decimal, decimal.Decimal(valor)
#num1 = decimal.Decimal('0.1')
#num2 = decimal.Decimal('0.7')
#num3 = num1 + num2
#print(num3) #0.8

num1 = 0.1
num2 = 0.7
num3 = num1 + num2
print(num3) #0.7999999999999999
print(round(num3, 2)) #0.8