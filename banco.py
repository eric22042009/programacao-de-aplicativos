import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escola (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXTO NOT NULL
        )
    ''')
    conexao.commit
    conexao.close()   