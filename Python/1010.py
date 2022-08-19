#---------- PEÇA 1 -----------
inteiro = input().split(" ")
inteiro2 = input().split(" ")


codigo_da_peca1, n_de_pecas1, valor_unitario1 = inteiro

#---------- PEÇA 2 ------------
codigo_da_peca2, n_de_pecas2, valor_unitario2 =  inteiro2



#---------- Calculando o preço para pagar ------------
total = ((int(n_de_pecas1) * float(valor_unitario1))) + ((int(n_de_pecas2) * float(valor_unitario2)))

#---------- Mostrando ------------
print("VALOR A PAGAR: R$", '%.2f'%total)