import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    try:
        query = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    
        cursor.execute (query, (id_registro,))
        resultado = cursor.fetchone()

        if resultado:
            print("Dados encontrados", resultado)

        else:
            print("Aviso: nenhun dado encontrado com esse ID")

    except sqlite3.OperationalError:
        print(f"aviso: A tabela '{nome_tabela}' não existe")
    
    finally:
        conexao.close()

buscar_dados_dinamicos('professores', 1)

#nao existe tratamento de erro caso o id nao exista, com o tratamento ele avia que não existe     