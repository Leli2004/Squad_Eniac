# atividade1:

numero1 = int(input(" digite o primeiro numero: "))
numero2 = int(input(" digite o segundo numero: "))
if numero1 > numero2:
    print(f"O numero {numero1} é o maior numero digitado")
else: 
    print(f"O numero {numero2} é o maior numero digitado")

#atividade2:
    
turno = (input(" Em que turno você estuda? Digite 'm' para manhã, 'v' para tarde, 'n' para noite):"))
if turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Entrada inválida por favor, digite 'm' para turno matutino,'v'para turno vespertino ou 'n' para noturno.")

#atividade3:
    
nota = (int(input("Digite sua nota entre 0 e 10: ")))
while (nota < 0) or (nota >= 10):
    nota = (int(input("Digite sua nota entre 0 e 10: ")))

#atividade4:
    
pontuacao_exame = (int(input(" Digite sua nota entre 0 e 10:")))
if pontuacao_exame >= 7:
    print("Aprovado")
elif pontuacao_exame <= 6:
    print("Reprovado")
else:
    print("Entrada inválida ")

#atividade5:

# equilátero:todos os lados com o mesmo valor 
# isósceles:dois lados com o mesmo valor 
# escaleno:todos os lados com medidas distintas

lado_a = (int(input("Insira a medida do primeiro lado:")))
lado_b = (int(input("Insira a medida do segundo lado:")))
lado_c= (int(input("Insira a medida do segundo lado:")))

if lado_a == lado_b == lado_c:
    print("É equilatero")
elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
    print("É isósceles")
elif (lado_a != lado_b) and (lado_b != lado_c) and (lado_c != lado_a):
    print("É escaleno ")
#ps: verificar como faz pra saber se nao é triangulo e adicionar um else ao final.