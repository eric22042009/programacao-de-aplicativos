import sqlite3


def buscar_professor(id_prof):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)
    conexao.commit()
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    if resultado:
        print("Professor encontrado:", resultado[0])
    else:
        print("Professor não encontrado!")
    conexao.close()


def inserir_professor(nome):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO professores (nome) VALUES (?)", ("nome,"))

    conexao.commit()
    conexao.close()


inserir_professor("Carlos")
buscar_professor(1)

# É obrigatorio colocar a virgula dps do elemento
