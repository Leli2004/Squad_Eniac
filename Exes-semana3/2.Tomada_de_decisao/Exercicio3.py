#atividade3:
    
nota = (int(input("Digite sua nota entre 0 e 10: ")))
while (nota < 0) or (nota > 10):
    print('Numero Inválido')
    nota = (int(input("Digite sua nota entre 0 e 10: ")))

