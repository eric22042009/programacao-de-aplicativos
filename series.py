import sqlite3

def cadastrar_series(nome_series, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    try:
        cursor.execute("INSER INTO series (nome_series, id_escola) VALUES (?, ?)",
(nome_series, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()
