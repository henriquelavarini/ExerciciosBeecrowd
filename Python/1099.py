#-------------------- Pegando informações
quantidade_casos = int(input())
soma_impares = 0
#-------------------- Casos de teste
#Pedindo para ele repetir esse laço a quantidade de vezes que quantidade_casos
for i in range(quantidade_casos):
    valor1, valor2 = input().split()
    valor1 = int(valor1)
    valor2 = int(valor2)
    if valor1 > valor2: #SE ele valo1 for maior que valor2
        for p in range(int(valor2) + 1, int(valor1)): #Pedindo para p ir de valor2 + 1 até valor1
            if p % 2 != 0: #Se p for ímpar
                soma_impares += p
    if valor1 < valor2: #Se o valor1 for menor que valor2
        for p in range(int(valor1) + 1, valor2): # Pedindo para p ir de valor1 + 1 até valor2
            if p % 2 != 0: #SE p for ímpar
                soma_impares += p #Somar soma_impares + p
    if valor1 == valor2:
        soma_impares = 0
    print(soma_impares) #Mostrar soma
    soma_impares = 0