import sqlite3


conexao = sqlite3.connect('banco') #conect ao arquivo biblioteca

cursor = conexao.cursor()


conexao.execute('CREATE TABLE Emprestimos (\
                id INTEGER PRIMARY KEY,\
                ISBN INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo DATE,\
                data_devolucao DATE,\
                Estado_do_Exemplar VARCHAR(30),\
                FOREIGN KEY(ISBN) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES(2,"2024-15-01","2024-06-02","Emprestado")')
cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES(5,"2024-13-02","2024-23-01","Devolvido")')
cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES(9,"2024-31-01","2024-06-02","Emprestado")')
cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES(1,"2023-15-12","2024-06-02","Atraso")')
cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES(10,"2024-05-02","2024-06-02","Emprestado")')

cursor.execute('ALTER TABLE Emprestimos ADD COLUMN título VARCHAR(60)')

cursor.execute('UPDATE Emprestimos SET título="O diário de Anne Frank" Where id="1"')
cursor.execute('UPDATE Emprestimos SET título="Pequeno manual Antirracista" Where id="2"')
cursor.execute('UPDATE Emprestimos SET título="Crime e Castigo" Where id="3"')
cursor.execute('UPDATE Emprestimos SET título="Dom Casmurro" Where id="4"')
cursor.execute('UPDATE Emprestimos SET título="De Ira" Where id="5"')



conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito