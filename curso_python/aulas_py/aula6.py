# conversão de tipos, coerção
# type convertion , type casting, coercion
# é um ato de converter um tipo a outro
# tipos imutáveis e primitivos 
# str, int, float, bool 
#print(int('1'), type(int('1'))) # converte string para inteiro
#print(float('1.0'), type(float('1.0'))) # converte string para float
#print(bool('1'), type(bool('1'))) # converte string para booleano

"""soma de string com inteiro:erro
soma de int com int = true
soma de float com float = true
soma de float com int = true"""

print(type(float('1') + 1)) # converte string para float e soma com inteiro
print(str(11) + 'b') # converte inteiro para string e concatena com string