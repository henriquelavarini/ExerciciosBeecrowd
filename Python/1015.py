#-------------- Importando a biblioteca math ----------------
import math

#-------------- Pedindo valores do eixo x e y----------------
#-------------- P1 -----------
x1, y1 = input().split(" ")
#-------------- Convertendo P1 para tipo float --------------
x1 = float(x1)
y1 = float(y1)

#-------------- P2 ------------
x2, y2 = input().split(" ")
x2 = float(x2)
y2 = float(y2)

#-------------- Calculando a distância entre os pontos-------
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#-------------- Apresentando a distancia ----------------
print('%.4f'%distancia)