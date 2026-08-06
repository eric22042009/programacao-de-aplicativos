import sqlite3


try:
    conexao = sqlite3.connect("id_cinemas.db")
    cursor = conexao.cursor 

    cursor.execute(" PRAGMA foreign_keys = ON;")

    cursor.execute("""
                 CREAT TABLE IF NOT EXIST cinemas(
                   INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,)
                     )

