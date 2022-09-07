#---------------------- Pegando informações --------------------
numero = int(input())

#---------------------- Vendo quais são os numeros pares e apresentando na tela
for i in range(1, numero+1):
    if i % 2 == 0:
        print('{}^2 = {}'.format(i, i**2))