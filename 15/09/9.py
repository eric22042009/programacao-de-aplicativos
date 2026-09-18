def busca_binaria_contando(vetor, alvo):
    esquer, direita = 0, len(vetor) - 1
    comparacoes = 0
    while esquer <= direita:
        comparacoes += 1
        meio = (esquer + direita) // 2
        if vetor[meio] == alvo:
            return meio, comparacoes
        elif vetor[meio] < alvo:
            esquer = meio + 1
        else:
            direita = meio - 1
    return -1, comparacoes
