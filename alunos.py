import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno: ")
  
    try:
        id_turma = int(input("digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)" (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Error no banco de dados!")
    except ValueError:
        print("digite um numero inteiro")
    finally:
        conexao.close()

        #so aicetava numero inteiro