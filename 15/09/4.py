def busca_nome(alunos, nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return True

    return False


alunos = ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"]

nome = input("Digite o nome que deseja buscar: ")

if busca_nome(alunos, nome):
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado.")
