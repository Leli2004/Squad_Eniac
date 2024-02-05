# classe livro

class Livro:
    def __init__(self, id, autor, titulo, editora, genero, quantidade_disponivel):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.quantidade_disponivel = 10

    def adicionarLivro(self, id, autor, genero):
        self.id = id

class Usuario:
    def __init__(self, id, nome, telefone, nacionalidade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def emprestaLivro(self, id, ):
        self.id = id
    
    def devolveLivro(self, id, ):
        self.id = id

class Emprestimo:
    def __init__(self, id, data_emprestimo,data_devolucao, estado_exemplar):
        self.id = id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado_exemplar = disponivel

