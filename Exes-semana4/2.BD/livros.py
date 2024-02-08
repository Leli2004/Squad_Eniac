import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()
# Criar uma tabela para os livros
cursor.execute('DROP TABLE Livros')
cursor.execute('CREATE TABLE Livros(id_Livros integer PRIMARY KEY AUTOINCREMENT,Titulo VARCHAR(50),Autor VARCHAR(50),Editora VARCHAR(50),Ano integer)')

conn.commit()
conn.close()

