#--------------- Pedindo os valores
x = int(input())
z = int(input())

#-------------- Pedindo o valor enquanto x for maior que z
while x >= z:
    z = int(input())

#-------------- Guardar o valor do x e guardando 1
guardar_x = x
adc_mais_um = 1
#--------------- Enquanto o valor guardado de x for menor que z, guardarx + adc_mais_um + x até guardarx ficar maior que z
while guardar_x < z:
    guardar_x += adc_mais_um + x
    adc_mais_um += 1

#---------------- Printar quantidade de vezes que foi aumentado o adc_mais_um
print(adc_mais_um)