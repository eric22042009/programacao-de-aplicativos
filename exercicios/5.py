import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    
    
    while True:
        try:
            id_turma = int(input("Digite o ID numerico da turma: "))
            break
        except ValueError:
            print("Erro: Digite apenas números! Tente novamente.\n")

    
    try:
        with sqlite3.connect('sistema_escola.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", 
                (nome, id_turma)
            )
            print(f"\nSucesso: Aluno '{nome}' vinculado à turma {id_turma}!")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")


vincular_aluno_turma()

#se a pessoa digitar letra ives de numero. mas com o while ele analisa e se nao for um numero ele avisa na tela 
#"Digite apenas números! Tente novamente"