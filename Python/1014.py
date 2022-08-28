#------------------ Pedindo informações ----------
distancia_percorrida = int(input())
total_combustivel = float(input())

#------------------ Calculando o consumo ---------
consumo = distancia_percorrida / total_combustivel

#------------------ Apresentando o consumo -------
print('%.3f'%consumo, "km/l")