def posicao_insercao(vetor, alvo):
    esquer, direita = 0, len(vetor) - 1
    while esquer <= direita:
        meio = (esquer + direita) // 2
        if vetor[meio] == alvo:
            return meio
        elif vetor[meio] < alvo:
            esquer = meio + 1
        else:
            direita = meio - 1
    return esquer
