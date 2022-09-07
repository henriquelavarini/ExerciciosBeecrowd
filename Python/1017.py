#--------------------- Informações --------------
tempo_gasto_viagem = int(input())
velocidade_media = int(input())
consumo_automovel = 12

#--------------------- Calculando a quantidade de litros necessarios para viagem

quantidade_em_litros = (tempo_gasto_viagem * velocidade_media) / consumo_automovel

#-------------------- Apresentando na tela
print('%.3f'%quantidade_em_litros)