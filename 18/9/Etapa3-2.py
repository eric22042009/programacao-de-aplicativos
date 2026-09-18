idade = int(input("Digite sua idade: "))

match idade:
    case i if i < 18:
        print("Acesso negado: Menor de idade.")
    case i if i >= 18:
        print("Acesso liberado.")
    case _:
        print("Idade inválida.")