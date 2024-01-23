# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração: 

# avião = 600km/h
# carro = 100km/h
# ônibus = 80km/h

def calcular_tempo(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

# Solicitar a distância da viagem ao usuário
distancia_viagem = float(input("Digite a distância da viagem em quilômetros: "))

# Calcular o tempo para avião, carro e ônibus
velocidade_aviao = 600
tempo_aviao = calcular_tempo(distancia_viagem, velocidade_aviao)

velocidade_carro = 100
tempo_carro = calcular_tempo(distancia_viagem, velocidade_carro)

velocidade_onibus = 80
tempo_onibus = calcular_tempo(distancia_viagem, velocidade_onibus)

print(f"Tempo estimado de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo estimado de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo estimado de viagem de ônibus: {tempo_onibus:.2f} horas")

