import sqlite3



try:
    conexao = sqlite3.connect("hospital.db")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais (id)
        )
    """
    )

    conexao.commit()
    print("Banco de dados criado")

except sqlite3.Error as e:
    print(f"Erro ao inicializar o banco de dados: {e}")
    
finally:
    if "conexao" in locals() and conexao:
        conexao.close()
        print("Conexão com o banco de dados fechada.")