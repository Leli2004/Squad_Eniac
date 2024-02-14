""" 4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
   - Dólar Americano: R$4,91
   - Peso Argentino: R$0,02
   - Dólar Australiano: R$3,18
   - Dólar Canadense: R$3,64
   - Franco Suíço: R$0,42
   - Euro: R$5,36
   - Libra esterlina: R$6,21  """

def converteParaMoedaEstrangeira(valorEmReais, taxaDeConversao):
    return valorEmReais / taxaDeConversao

def converteDinheiroParaMoedasEstrangeiras():
    carteiraEmReais = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))
    
    moedas = { 
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suíço': 0.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21
    }

    print(f"Com R${carteiraEmReais:.2f} você poderia comprar:")

    for moeda, taxa in moedas.items():
        moedaEstangeira = converteParaMoedaEstrangeira(carteiraEmReais, taxa)
        print(f" - {moeda}: {moedaEstangeira:.2f}")

converteDinheiroParaMoedasEstrangeiras()