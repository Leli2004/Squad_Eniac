# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somando():
    # Solicita 3 input
    num1 = float(input('Informe o 1° número: '))
    num2 = float(input('Informe o 2° número: '))   
    num3 = float(input('Informe o 3° número: '))  

    # Calculando a soma
    soma = num1+num2+num3

    # Imprimindo o resultado
    print(f'O resultado da soma é: {soma}')

# Chamando a função
somando()