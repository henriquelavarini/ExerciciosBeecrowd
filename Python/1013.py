#----------- Importando biblioteca -----------
import math

#----------- Pedindo um valor e separando eles por espaçoes com split
valor = input().split(" ")
valor1, valor2, valor3 = valor

#----------- Calculando o maior numero entre o valor1 e valor2
maior = (int(valor1) + int(valor2) + abs(int(valor1) - int(valor2)))/2
#----------- Calculando o maior numero entre o valor1, valor2 e valor3
resultado = (int(maior) + int(valor3) + abs(int(maior) - int(valor3)))/2

#----------- Apresentando o maior valor
print("%d eh o maior" %resultado)