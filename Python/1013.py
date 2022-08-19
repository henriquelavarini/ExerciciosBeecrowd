import math

valor = input().split(" ")
valor1, valor2, valor3 = valor

maior = (int(valor1) + int(valor2) + abs(int(valor1) - int(valor2)))  / 2
resultado = (int(maior) + int(valor3) + abs(int(maior) - int(valor3)))/2

print("%d eh o maior" %resultado)