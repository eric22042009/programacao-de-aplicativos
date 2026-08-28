turma = []

while True:
    print("1 - Adicionar Aluno")
    print("2 - Mostrar Turma")
    print("3 - Sair")

    opcao = input("digite a opção: ")

    if opcao == "1":
        nome = input("digite o nome: ")
        turma.append(nome)  #ADICIONA OQ ESTA GURDADO NA VARIAVEL

    elif opcao == "2":
        n = 1
        for aluno in turma:   #PERCORRE OQ ESTA SALVO ENTRO DA LISTA TURMA 
            print(n, "Aluno:", aluno)
            n += 1

    elif opcao == "3":
        break
