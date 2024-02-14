horas_por_semana = float(input('Digite o número de horas de exercício físico por semana: '))

minutos_por_semana = horas_por_semana * 60
calorias_por_minuto = 5
calorias_por_semana = minutos_por_semana * calorias_por_minuto
calorias_por_mes = calorias_por_semana * 4

print('O total de calorias queimadas em um mês é: ', calorias_por_mes)