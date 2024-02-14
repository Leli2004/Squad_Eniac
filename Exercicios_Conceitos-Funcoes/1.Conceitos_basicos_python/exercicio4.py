print('Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.')

l = int(input('LITROS: '))
dist = float(input('DISTANCIA: '))

media = l / dist 

print(f'{media:.2f}')