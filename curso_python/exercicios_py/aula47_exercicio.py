
import os

palavra_secreta = ('nomade')
letras_acertadas = ''
numero_tentativas = 0

while True:
   
    letra_digitada = input('Digite uma letra: ').lower().strip()
    if len(letra_digitada) != 1 or not letra_digitada.isalpha():
        print('Digite apenas UMA LETRA VÁLIDA')
        continue

    numero_tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    elif letra_digitada not in palavra_secreta: 
        print(f'A letra {letra_digitada} não está na palavra secreta.')
        

    palavra_formada = '' 

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:

        os.system('clear')
        print('VOCÊ GANHOU!!!')
        print('A palavra era ' , palavra_formada)
        print(f'a quantidade de tentativas foi {numero_tentativas}x')
        break