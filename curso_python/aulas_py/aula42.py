frase = 'O Python é uma linguagem de programação'  \
          'Multiparadigma.' \
          'Python foi criado por Guido van Rossum.'.lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):

    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
   
    if letra_atual == ' ':
         i += 1
         continue


    if qtd_apareceu_mais_vezes < qtd_atual:
        
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual


    i += 1

print(
    'A letra que apareceu mais vezes foi: '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f' {qtd_apareceu_mais_vezes}'
)
