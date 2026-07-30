import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT INTO escolas (id, nome) VALUES (?, ?)",
        (id_escola, nome)
    )

    conexao.commit()
    conexao.close()

cadastrar_escola_manual()


# fechar a conexão e chamar a função