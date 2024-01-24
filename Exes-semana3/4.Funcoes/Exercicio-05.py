'''Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e
utilize a função para contar as vogais.'''

#Funcao

def conta_vogais(string):
    string = string.lower() 
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais) 
    
print(conta_vogais(input('Digite a frase para contar as vogais: ')))

