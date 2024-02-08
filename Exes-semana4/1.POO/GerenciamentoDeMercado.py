#2. **OPÇÃO 2: Gerenciamento de Mercado**
#    Vamos criar um sistema orientado a objetos para representar um sistema de mercado seguindo os requisitos fornecidos
#    - Cada livro pode ter um ou mais autores;
#    - O mercado controla apenas o nome, o telefone e o endereço de cada cliente;
#    - Cada produto tem um nome, uma lista de categorias às quais pertence e uma quantidade disponível em estoque;
#    - Quando um produto é comprado, sua quantidade disponível em estoque é reduzida;
#    - O mercado mantém um registro de todas as transações realizadas, incluindo detalhes como data da compra, cliente envolvido e quantidade de produtos comprados;

from datetime import datetime

class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autores, categorias, quantidade_disponivel):
        self.titulo = titulo
        self.autores = autores  # Lista de objetos da classe Autor
        self.categorias = categorias  # Lista de categorias
        self.quantidade_disponivel = quantidade_disponivel

    def comprarLivro(self, quantidade):
        if quantidade <= self.quantidade_disponivel:
            self.quantidade_disponivel -= quantidade
            return True
        else:
            return False

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Transacao:
    def __init__(self, cliente, produtos_comprados):
        self.data_compra = datetime.now()
        self.cliente = cliente  # Objeto da classe Cliente
        self.produtos_comprados = produtos_comprados  # Lista de objetos da classe Livro

# Exemplo de uso:
# Criando autores
autor1 = Autor("Autor1")
autor2 = Autor("Autor2")

# Criando livros
livro1 = Livro("Livro1", [autor1], ["Ficção", "Aventura"], 50)
livro2 = Livro("Livro2", [autor1, autor2], ["Romance"], 30)

# Criando cliente
cliente1 = Cliente("Cliente1", "123456789", "Rua A, 123")

# Comprando livros
livro1.comprarLivro(5)
livro2.comprarLivro(10)

# Registrando transação
transacao1 = Transacao(cliente1, [livro1, livro2])

for produto in transacao1.produtos_comprados:
    print("- Título:", produto.titulo)
    print("  Autores:", [autor.nome for autor in produto.autores])
    print("  Categorias:", produto.categorias)
    print("  Quantidade Comprada:", 10)  # Assumindo que a quantidade comprada foi 10 para todos os produtos
    print("----------------------")