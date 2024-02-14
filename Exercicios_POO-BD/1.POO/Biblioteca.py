# classe livro

class Livro:
    def __init__(self, id, autor, titulo, editora, genero, quantidade_disponivel):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.quantidade_disponivel = 10

    def adicionarLivro(self, id, autor, titulo,editora, genero, quantidade_disponivel):
        print("adicionando um livro")
    
    def excluirLivro(self, id, titulo):
        print("Livro excluido")

    def editarLivroAdicionado(self, id):
        print("Livro atualizado")
    
    def consultarLivro(self, autor, genero):
        print("Livros disponiveis")

class Usuario:
    def __init__(self, id, nome, telefone, nacionalidade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
    
    def emprestarLivro(self, nome):
        print(f'{nome} emprestou um livro')
    
    def devolverLivro(self, nome ):
        print(f'{nome} devolveu um livro')


class Emprestimo:
    def __init__(self, id, data_emprestimo,data_devolucao, estado_exemplar):
        self.id = id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado_exemplar = disponivel

    def retiradaDeLivro(self, id, data_emprestimo,disponivel):
        print(f'Livro retirado na data {data_emprestimo}, false')
    
    def devolucaoDeLivro(self, id, data_devolucao):
        print(f'Livro devolvido na data {data_devolucao}, false')

    def consultarEmprestimo(self, id, nome, data_emprestimo):
        print(f'Registro dos livros devolvidos e emprestado')

l1 = Livro(1, "manoel bandeira", "Aurora", "Atlas", "literatura", 12)
l1.adicionarLivro(1, "manoel bandeira", "Aurora", "Atlas", "literatura", 12)
l1.excluirLivro(1, "aurora")

u1 = Usuario(1, "Alexandre Dimas", 129923457, "brasileiro")
u1.emprestarLivro("Alexandre Dimas")

e1 = Emprestimo(1, 12012024,12022024, "emprestado")
e1.retiradaDeLivro(1, 12012024, "emprestado")
e1.emprestimo()