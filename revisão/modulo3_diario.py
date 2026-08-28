turma = []

while True:
    print("1 - Adicionar Aluno")
    print("2 - Mostrar Turma")
    print("3 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        turma.append(nome)

    elif opcao == "2":
        n = 1
        for aluno in turma:
            print(n, "Aluno:", aluno)
            n += 1

    elif opcao == "3":
        break
