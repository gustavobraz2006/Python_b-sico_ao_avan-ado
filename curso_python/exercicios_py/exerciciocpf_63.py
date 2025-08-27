cpf = input ("Digite o CPF (somente números): ")
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido. Certifique-se de digitar 11 números.")
    exit()
nove_digitos = cpf[:9]
contador_regressivo = 10
soma = 0

for digito in nove_digitos:
   resultadomult = digito * contador_regressivo
   contador_regressivo -= contador_regressivo 
   soma += resultadomult

   print(soma)

print(soma)