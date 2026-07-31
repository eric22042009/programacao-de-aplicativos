def menu():
    while True:
        print("1. cadastrar aluno")
        print("2. sair")
        opcao = input("escolha: ")

        if opcao == "1":
            print("cadastrando...")
        elif opcao == "2":
            print("sindo do programa.")
            break
            
#falto o 'break'