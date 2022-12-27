#-------------------- Quantidade de valores positivos iniciais
valores_positivos = 0

#------------------------ Pegando informações
#------------------------ Para cara valor de 1 a 6
for valores in range(1,7):
    valores = float(input())
#------------------------ Se os valores forem maior que 0
#------------------------ Adicionar +1 no contador valores_positivos
    if valores > 0:
        valores_positivos += 1

#------------------------ Apresentando os valores positivos
print('{} valores positivos'.format(valores_positivos))