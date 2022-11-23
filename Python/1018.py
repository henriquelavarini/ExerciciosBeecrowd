#--------------- Pedindo um numero inicial
notas1 = int(input())
print(notas1)

#--------------- Dividindo o valor1 por 100
notas100 = notas1//100
notas1 = notas1%100

#--------------- Dividindo o valor1 por 50
notas50 = notas1//50
notas1 = notas1%50

#--------------- Dividindo o valor1 por 20
notas20 = notas1//20
notas1 = notas1%20

#--------------- Dividindo o valor1 por 10
notas10 = notas1//10
notas1 = notas1%10

#--------------- Dividindo o valor1 por 5
notas5 = notas1//5
notas1 = notas1%5

#--------------- Dividindo o valor1 por 2
notas2 = notas1//2
notas1 = notas1%2

print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")