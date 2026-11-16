import sqlite3

conexao = sqlite3.connect('database/fintrack.db')
cursor = conexao.cursor()
def cadastrar(nome, email=None):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)",
        (nome, email))
    conexao.commit()
    
cadastrar('Caio')
conexao.close()