'''CONSTANTE = "Váriaveis" que não vão mudar
muitas condições no mesmo if(ruim)
    <- contagem de complexidade(ruim)
    '''

velocidade = 56 #velocidade atual do carro
local_carro = 101 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #distância onde o radar pega

if velocidade > RADAR_1:
    print('Você ultrapassou a velocidade máxima do radar 1')

    if (local_carro == LOCAL_1 + RADAR_RANGE) or (local_carro == LOCAL_1 - RADAR_RANGE) or (local_carro == LOCAL_1):    
        print ('Você foi multado.')

    else:
        print('Sem violação de trânsito')

else:
    print('Velocidade permitida')


    