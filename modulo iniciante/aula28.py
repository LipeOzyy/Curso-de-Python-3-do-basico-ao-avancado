"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_car_pass_radar1 = velocidade > RADAR_1
car_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = car_passou_radar1 and velocidade_car_pass_radar1


if velocidade_car_pass_radar1:
    print('A velocidade do veiculo ultrapassou o limite do radar')
else:
    print('A velocidade do carro está dentro do limite permido')

if car_passou_radar1:
    print('O veiculo passou no 1 radar')

if local_carro >= car_passou_radar1 and velocidade_car_pass_radar1:
    print('O veiculo foi multado')
else:
    print('O veiculo não foi multado')