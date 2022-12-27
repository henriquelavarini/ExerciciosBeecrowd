#-------------- Pedindo o tempo em segundos
segundos = int(input())
#-------------- Convertendo os segundos em horas, mas pegando so a parte inteira da divisão
horas = segundos // (60**2)
#-------------- Passando o resto da divisão da divisão para o tempo
segundos = segundos % 60**2
#-------------- Convertendo os segundos em minutos, mas pegando so a parte inteira da divisão
minutos = segundos // 60
#-------------- Passando o resto da divisão dos minutos para o tempo
segundos = segundos % 60
#-------------- Mostrando na tela o tempo final
print("{}:{}:{}".format(horas, minutos, segundos))

