import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# Criando tabela na biblioteca

cursor.execute('CREATE TABLE livros(id INTEGER PRIMARY KEY, autor VARCHAR(100), título VARCHAR(100), cópias INT, editora VARCHAR(100), ISBN INT, máximo_renovações INT);')

# Inserindo VALUES na tabela livros

cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Gabriel García Márquez","Cem anos de solidão",50,"RECORD",001002001,4)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Clarice Lispector","Água Viva",30,"ROCCO",001002002,10)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Clarice Lispector","A hora da estrela",45,"ROCCO",001002003,20)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Machado de Assis","Dom Casmurro",22,"Thoth",001002004,3)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Machado de Assis","Memórias Póstumas de Brás Cubas",15,"Antofágica",001002005,9)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Fiódor Dostoévski","Crime e Castigo",10,"Editora 34",001002006,2)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Djamila Ribeiro","Pequeno manual Antirracista",50,"Companhia das Letras",001002007,35)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Anne Frank","O diário de Anne Frank",10,"RECORD",001002008,2)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("J. K. Rowling","Harry Potter. E a pedra Filosofal",20,"Bloomsbury Publishing",001002009,9)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Cecília Meirelles","O menino azul",10,"Global Editora",001002010,9)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Sêneca","De Ira",5,"Camelot Editora",001002011,2)')
cursor.execute('INSERT INTO livros(autor, título, cópias, editora, ISBN, máximo_renovações) VALUES("Aldous Huxley","Admirável mundo novo",6,"Biblioteca Azul",001002012,2)')

#dados = cursor.execute('DROP TABLE livros')
#for biblioteca in dados:
 #    print(biblioteca)

conexao.commit()
conexao.close

