#------------ Pedindo valores ---------
valor = float(input())

#----------- Verificando se esta dentro dos intervalos
#----------- Apresentando
if (valor >= 0) and (valor <= 25):
    print("Intervalo [0,25]")
else:
    if (valor >= 25) and (valor <= 50):
        print("Intervalo (25,50]")
    elif (valor >=50) and (valor <= 75):
        print("Intervalo (50,75]")
    elif (valor >= 75) and (valor <= 100):
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")