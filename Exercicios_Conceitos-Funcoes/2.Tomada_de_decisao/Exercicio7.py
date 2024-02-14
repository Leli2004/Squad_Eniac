# Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.

idade = int(input("Qual é a sua idade?  "))

def classificacao_idade(idade):

    if idade < 0:
        return "Criança!"

    elif idade < 18:
        return "Adolecente"

    elif idade < 60:
        return "Adulto"

    else:
        return "Idoso"
    
classificacao = classificacao_idade(idade)

print(f'Você é classificado como {classificacao}.')    