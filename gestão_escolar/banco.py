import sqlite3


def conectar():
    conexao = sqlite3.connect("gestao_escolar.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
            id_escola INTEGER NOT NULL,
            FOREING KEY (id_escola) REFERENCES escola.id
        )
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            idade INTEGER NOT NULL
            id_turma INTTEGER NOT NULL
            FOREING KEY (id_turma) REFERENCES escola.id
        )
        ''')
    
    conexao.commit
    conexao.close