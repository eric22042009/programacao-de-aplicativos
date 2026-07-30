import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    print(cursor.fetchone())
    conexao.close()