""" 8. Criar um programa em Python que solicite três números ao usuário, 
utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado. """

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))


if numero1 == numero2 == numero3: 
    print('Os números são iguais')

elif numero1 > numero2 and numero1 > numero3: 
    print(f'{numero1} é o maior ')

elif numero2 > numero3:
    print(f'{numero2} é o maior ')
 
else:
    print(f'O {numero3} é maior')
    