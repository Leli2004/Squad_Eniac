#08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.#

# Pergunta ao usuário o valor ganho por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas_por_mes = float(input("Quantas horas você trabalha por mês? "))

# Calcula o salário total
salario_total = valor_por_hora * horas_trabalhadas_por_mes

# Mostra o resultado
print(f"Seu salário total no mês é: R$ {salario_total:.2f}")