""" Solicite ao usuário o peso em kg e a altura em metros. 
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC=peso/(alturaxaltura). """

peso = float(input('Digiti o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

# IMC
imc = peso / (altura * altura)
print(f'O seu IMC é {imc} .')
