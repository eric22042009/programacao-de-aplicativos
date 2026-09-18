dia = input("Digite o dia da semana: ").lower()

match dia:
    case "sábado" | "domingo":
        print("Fim de semana!")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil!")
    case _:
        print("Dia inválido.")