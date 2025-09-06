cpf_enviado_cliente = input("Digite o CPF (somente números): ").replace('.', '')\
.replace(' ', '')\
.replace('-', '') 
if len(cpf_enviado_cliente) != 11 or not cpf_enviado_cliente.isdigit():
    print("CPF inválido. Certifique-se de digitar 11 números.")
    exit()
nove_digitos = cpf_enviado_cliente[:9]
contador_regressivo = 10
soma = 0

for digito in nove_digitos:
   resultadomult = int(digito) * contador_regressivo
   contador_regressivo -= 1
   soma += resultadomult

getMultiplica_10 = soma * 10
getResto_divisao = getMultiplica_10 % 11

if(getResto_divisao > 9):
    primeiroDigito = 0
else:
    primeiroDigito = getResto_divisao

print(primeiroDigito)

dez_digitos = cpf_enviado_cliente[:10]
contador_regressivo2 = 11 
soma2 = 0

for digito in dez_digitos:
    resultadomult2 = int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
    soma2 += resultadomult2
    
get2Multiplica_10 = soma2 * 10
get2Resto_divisao = get2Multiplica_10 % 11
if(get2Resto_divisao > 9):
    segundoDigito = 0
else:
    segundoDigito = get2Resto_divisao

print(segundoDigito)
cpf_calculado = str((f'{nove_digitos}{primeiroDigito}{segundoDigito}'))

if(cpf_enviado_cliente == cpf_calculado):
    print('CPF é válido')

else:
    print('CPF é inválido')