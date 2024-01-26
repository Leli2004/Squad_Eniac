#exercicio 5 
    
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