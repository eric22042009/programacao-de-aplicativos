import sqlite3

conexao = sqlite3.connect("escola_sistema.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT,
    nota REAL
)
""")

while True:
    print("\n1 - Cadastrar Aluno")
    print("2 - Listar Todos")
    print("3 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        curso = input("Curso: ")
        nota = input("Nota: ")

        comando = f"INSERT INTO alunos (nome, curso, nota) VALUES ('{nome}', '{curso}', {nota})"
        cursor.execute(comando)
        conexao.commit()

        print("Aluno cadastrado!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        for aluno in alunos:
            print(aluno)

    elif opcao == "3":
        break

conexao.close()
