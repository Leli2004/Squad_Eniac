'''Crie um dicionário representando um carrinho de compras.
Adicione produtos(chaves) e quantidades(valores) ao carrinho.
Calcule o total do carrinho de compra.'''

#Carrinho de compras

dicionario = {}
dicionario['leite'] = 5.99
dicionario['macarrão'] = 9.80
dicionario['arroz'] = 9.55
dicionario['milho'] = 2.90

#Calcular valores
total = sum(dicionario.values())

print(f'O total do carrinho de compras é: {total:.2f}')