numeros = list(range(1, 101))


def busca_sequencial(lista, procurado):
    comparacoes = 0

    for numero in lista:
        comparacoes += 1

        if numero == procurado:
            print("Busca Sequencial:")
            print("Número encontrado:", procurado)
            print("Comparações:", comparacoes)
            return


def busca_binaria(lista, procurado):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == procurado:
            print("\nBusca Binária:")
            print("Número encontrado:", procurado)
            print("Comparações:", comparacoes)
            return

        elif lista[meio] < procurado:
            inicio = meio + 1

        else:
            fim = meio - 1


busca_sequencial(numeros, 95)
busca_binaria(numeros, 95)
