''' Reverso do número. 
    Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''
def inverte(numero):
    # Convertendo para string para facilitar a inversão
    numero_str = str(numero)
    
    # Invertendo a string
    numero_invertido = numero_str[::-1]
    
    # Convertendo de volta para inteiro
    numero_invertido = int(numero_invertido)
    
    return numero_invertido

numero_original = str(input('\nInforme um número inteiro: '))

numero_reverso = inverte(numero_original)

print(f'\nO reverso de {numero_original} é {numero_reverso}')
