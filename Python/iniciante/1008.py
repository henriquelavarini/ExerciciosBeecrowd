#------------- Pedindo informações (numero do funcionario, horas de trabalho e valor das horas de trabalho)
numero = int(input())
horas_trabalho = int(input())
valor_hora_trabalho = float(input())

#------------- Mostrando do numero do funcionario
print("NUMBER =", numero)

#------------- Calculando o salario das horas de trabalho pelo valor da hora de trabalho
salario = horas_trabalho * valor_hora_trabalho

#------------- Mostrando o salário
print("SALARY = U$", '%.2f'%salario)