'''Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário detrás para frente utilizando somente letras maiúsculas.
Dica:lembre se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

#Usuario digitar nome
print("Descubra como fica seu nome invertido em letra maiuscula \n")
nome = input("Digite seu nome (podem ser usadas letras maiusculas ou minusculas): " );

#Mostrar nome de tras para frente com letras maiusculas
nome_invertido = nome[::-1]
invertido_maiuscula = nome_invertido.upper()
print(f'Seu nome invertido em letras maiusculas é: {invertido_maiuscula}')