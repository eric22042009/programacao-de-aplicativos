import sqlite3


conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT
    )
""")
conexao.commit()


while True:
    print("---menu---")
    print("1. cadastrar livros:")
    print("2. listar livros:")
    print("3. sair")

    opcao = input("escolha uma opção")

    try:
        if opcao == "1":
            titulo = input("titulo:")
            autor = input("autor:")
            
            cursor.execute(
                "INSERT INTO livros (titulo, autor) VALUES (?, ?)", (titulo, autor)
            )
            conexao.commit()
            print("livros cadastrados com sucesso")

        elif opcao == "2":
            cursor.execute("select*from livros") 
            livros = cursor.fetchall()
            print("---lista de livro---")
           
            for (l) in livros:
                print(l)
           

        elif opcao == "3":
            conexao.close()
            print("saindo.")
            break

    except Exception as e:
        print("erro", e)



