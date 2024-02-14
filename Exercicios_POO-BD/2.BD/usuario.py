import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('banco') #conect ao arquivo biblioteca

cursor = conexao.cursor()

#Criar uma tabela para os usuarios
conexao.execute('CREATE TABLE Usuarios (\
                id INTEGER PRIMARY KEY,\
                nome VARCHAR(100),\
                telefone INT,\
                nacionalidade VARCHAR(30))')

cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Emanoella",22110221,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Elisa",551109999,"Americana")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Amanda",11220221,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Mônica",09991121,"Francesa")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Luiza",99996666,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Laura",144440221,"Americana")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Melina",33220221,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Roberta",663310221,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Thaynene",76540221,"Francesa")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Maria Flor",99552291,"Brasileira")')
cursor.execute('INSERT INTO Usuarios(nome,telefone,nacionalidade) VALUES("Yasmin",992233311,"Brasileira")')

conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito