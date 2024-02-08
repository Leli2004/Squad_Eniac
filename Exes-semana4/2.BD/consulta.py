import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('banco') #conect ao arquivo biblioteca

cursor = conexao.cursor()
#ATIVIDADE1 FEITA
# - Listar todos os livros disponíveis
# dados = cursor.execute('SELECT * FROM livros')
# for livros in dados:
#     print(livros)

# Encontrar todos os livros emprestados no momento

# dados2 = cursor.execute('SELECT * FROM Emprestimos WHERE Estado_do_Exemplar= "Emprestado"')
# for livros in dados2:
#      print(livros)

# dados = cursor.execute('SELECT * FROM Emprestimos GROUP BY Estado_do_Exemplar HAVING Estado_do_Exemplar="Emprestado" ')
# for livros in dados:
#     print(livros)

# Localizar os livros escritos por um autor específico
# dados = cursor.execute('SELECT * FROM Livros WHERE autor= "Anne Frank"')
# for livros in dados:
#     print(livros)

# Verificar o número de cópias disponíveis de um determinado livro
# dados1 = cursor.execute('SELECT cópias FROM livros WHERE título="Dom Casmurro"')
# for livros in dados1:
#     print(livros)
# Mostrar os empréstimos em atraso.

# dados3 = cursor.execute('SELECT título FROM Emprestimos WHERE Estado_do_Exemplar="Atraso"')
# for livro in dados3:
#     print(livro)

# delete remover um autor
# cursor.execute('DELETE  FROM Livros WHERE autor ="Clarice Lispector"')
# remover um livro

# cursor.execute('DELETE FROM livros WHERE título="O menino azul"')
# marcar um livro como devolvido

# dados4 = cursor.execute('SELECT título FROM Emprestimos WHERE Estado_do_Exemplar="Devolvido"')
# for livro in dados4:
#     print(livro)


conexao.commit()
conexao.close()