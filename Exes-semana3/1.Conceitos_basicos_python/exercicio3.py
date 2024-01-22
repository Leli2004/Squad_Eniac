print('Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.')

km = float(input('KM: '))
m = km * 1000
cm = km * 100000
mm = km * 1000000

print(f'{km} quilometros é igual a: ')
print(f'{m} metros')
print(f'{cm} centímetros')
print(f'{mm} milimetros')