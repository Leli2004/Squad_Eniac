impar = par = 0
print("Digite 0 para encerrar o programa")
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero > 0:
      if numero != 0:
        if numero % 2 ==0:
          par += 1
        else:
          impar += 1
    else:
      print("Número não aceito, digite apenas números positivos")
print(f"Você digitou {par} números pares e {impar} números ímpares ")