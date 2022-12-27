#---------------- Pedindo valores -----------
valor1, valor2, valor3 = input().split(" ")
valor1 = float(valor1)
valor2 = float(valor2)
valor3 = float(valor3)
pi = 3.14159

#---------------- CALCULANDO ----------------
#---------------- A) Área do triângulo
#---------------- Base: valor1 
#---------------- Altura: valor3
triangulo = (valor1 * valor3) / 2

#---------------- B) Área do circulo:
#---------------- Raio: valor3
circulo = pi * (valor3**2)

#---------------- C) Área do trapézio
#---------------- Bases: valor1 e valor2
#---------------- Altura: valor3
trapezio = ((valor1 + valor2) * valor3) / 2

#---------------- D) Área do quadrado
#---------------- Lado = valor2
quadrado = valor2**2

#---------------- Área do retângulo
#---------------- Lados: valor1 e valor2
retangulo = valor1 * valor2

#---------------- Mostrando os valores -----------
print(f"TRIANGULO: {triangulo:.3f}\n" "CIRCULO: {circulo:.3f}\n" "TRAPEZIO: {trapezio:.3f}\n" "QUADRADO: {quadrado:.3f}\n" "RETANGULO: {retangulo:.3f}".format(triangulo = triangulo, circulo = circulo, trapezio = trapezio, quadrado = quadrado, retangulo = retangulo))