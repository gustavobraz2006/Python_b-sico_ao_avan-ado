''' Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>
x ou X - Hexadecimal
(Caractere) (<>)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= Força o número aparecer antes dos zeros
Sinal - + ou -
Ex.: 0 > -100,.1f
Conversion flags - !r !s !a
'''
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')#pula 7 espaços na esquerda contando com 3 caracteres abc = 10c
print(f'{variavel: <10}')#pula 7 espaços na direita contando com 3 caracteres abc = 10c
print(f'{variavel: ^10}')#tenta colocar no centro
print(f'{1004.40240242:0=+10,.1f}') # +001,004.4
print(f'O hexadecimal de 100 é {100:04x}')