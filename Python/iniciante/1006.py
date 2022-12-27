#------------- Pedindo informação (notas) -----------
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

#----------- Calculando média com peso (2, 3, 5)
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5))/(2+3+5)

#----------- Apresentando
print("MEDIA =",  "%.1f" % media)
