import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # Sem o execute o cursor nao tem nenhum resultado 
    
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?", (id_registro,))
    print(cursor.fetchone())
    conexao.close()

buscar_dados_dinamicos('professores', 1)