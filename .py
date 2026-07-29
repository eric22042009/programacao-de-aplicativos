import sqlite3

# ==========================
# BANCO DE DADOS
# ==========================
conexao = sqlite3.connect("professores.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS professores (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    materia TEXT NOT NULL,
    numero INTEGER NOT NULL,
    senha TEXT NOT NULL
)
""")

conexao.commit()


# ==========================
# CADASTRAR
# ==========================
def cadastrar():

    print("\n===== CADASTRO =====")

    nome = input("Nome do professor: ")

    while True:
        cpf = input("CPF (somente números): ")

        if cpf.isdigit():
            break
        else:
            print("Digite apenas números!")

    cursor.execute("SELECT * FROM professores WHERE cpf = ?", (cpf,))
    professor = cursor.fetchone()

    if professor:
        resposta = input("CPF já cadastrado. Deseja atualizar o cadastro? (S/N): ").upper()

        if resposta != "S":
            return

    materia = input("Matéria: ")

    while True:
        try:
            numero = int(input("Digite um número entre 1 e 11: "))

            if 1 <= numero <= 11:
                break
            else:
                print("O número deve estar entre 1 e 11.")

        except ValueError:
            print("Digite apenas números.")

    senha = input("Crie uma senha: ")

    cursor.execute("""
    INSERT OR REPLACE INTO professores
    (cpf, nome, materia, numero, senha)
    VALUES (?, ?, ?, ?, ?)
    """, (cpf, nome, materia, numero, senha))

    conexao.commit()

    print("\nCadastro salvo com sucesso!")


# ==========================
# ACESSAR CADASTRO
# ==========================
def acessar():

    print("\n===== ACESSAR =====")

    cpf = input("CPF: ")
    senha = input("Senha: ")

    cursor.execute("""
    SELECT nome, materia, numero
    FROM professores
    WHERE cpf=? AND senha=?
    """, (cpf, senha))

    dados = cursor.fetchone()

    if dados:

        print("\n===== DADOS =====")
        print("Nome:", dados[0])
        print("CPF:", cpf)
        print("Matéria:", dados[1])
        print("Número:", dados[2])

    else:
        print("CPF ou senha incorretos.")


# ==========================
# LISTAR TODOS
# ==========================
def listar():

    cursor.execute("SELECT cpf, nome, materia FROM professores")

    lista = cursor.fetchall()

    if len(lista) == 0:
        print("\nNenhum cadastro encontrado.")
        return

    print("\n===== PROFESSORES CADASTRADOS =====")

    for professor in lista:
        print(f"CPF: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Matéria: {professor[2]}")
        print("-" * 30)


# ==========================
# EXCLUIR
# ==========================
def excluir():

    cpf = input("Digite o CPF para excluir: ")

    cursor.execute("SELECT * FROM professores WHERE cpf=?", (cpf,))
    existe = cursor.fetchone()

    if not existe:
        print("CPF não encontrado.")
        return

    cursor.execute("DELETE FROM professores WHERE cpf=?", (cpf,))
    conexao.commit()

    print("Cadastro excluído com sucesso.")


# ==========================
# MENU
# ==========================
while True:

    print("\n========== MENU ==========")
    print("1 - Cadastrar Professor")
    print("2 - Acessar Cadastro")
    print("3 - Listar Professores")
    print("4 - Excluir Cadastro")
    print("5 - Sair")

    try:

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            acessar()

        elif opcao == 3:
            listar()

        elif opcao == 4:
            excluir()

        elif opcao == 5:
            print("Programa encerrado.")
            break

        else:
            print("Escolha uma opção válida.")

    except ValueError:
        print("Digite apenas números.")

conexao.close()