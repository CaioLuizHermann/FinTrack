import sqlite3

conexao = sqlite3.connect('database/fintrack.db')

cursor = conexao.cursor()

cursor.execute("SELECT id, email, data_cadastro, nome FROM clientes")

dados = cursor.fetchall()
print(dados)