print('Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão.')

n1 = int(input('Insira seu primeiro número: '))
n2 = int(input('Agora o segundo número: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print(f'A soma é {soma}')
print(f'A subtração é {sub}')
print(f'A multiplicação é {mult}')
print(f'A divisão é {div:.0f}')