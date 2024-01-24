    #2.Tomada de Decisao e Repeticao
    #10. Faça um programa que lê três números inteiros e os mostra em ordem crescente
    
    # Solicita 3 numeros
a = int(input('Digite primeiro número: '));
b = int(input('Digite segundo número: '));  
c = int(input('Digite terceiro número: '));

print(f' Numeros digitados: {a}, {b}, {c} ');

if a > c:
    a, c = c, a

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

print(f' Numeros ordenados: {a}, {b} e {c} ');
