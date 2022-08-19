#----------- Pedindo informações (nome, salario fixo e total de vendar no mes) ----------
nome_vendedor = input()
salario_fixo = float(input())
total_venda_mes = float(input())

#----------- Calculando o salario total no mês
total = salario_fixo + (total_venda_mes * (15/100))

#----------- Apresentando
print("TOTAL = R$", '%.2f'%total)