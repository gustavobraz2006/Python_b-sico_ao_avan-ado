#operadores lógicos
#and (e) or (ou) not (não)
#and - todas as condições precisam ser verdadeiras
#se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
#São consideradas falsy(que voce ja viu)
#0 0.0 '' False
# também existe  o tipo None que é
#usado para representar um não valor

entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = '123456'
#if condição dado booleano

if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrar')
else:
    print('Sair')

