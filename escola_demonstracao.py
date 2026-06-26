def cadastrar_usuario():
    nome = input("nome?: ")
    telefone = input("qual seu telefone?: ")
    idade = int(input("idade?: "))
    cpf = input("CPF: ")
    salario = input("salario: ")
    nome_da_escola = input("nome da escola: ")

    if idade < 18:
        print("cadastro recusado--")
    else: 
         print("--cadastro aceito--")

    print(nome)
    print(telefone)
    print(idade)
    print(cpf)
    print(salario)
    print(nome_da_escola)
   
cadastrar_usuario()

