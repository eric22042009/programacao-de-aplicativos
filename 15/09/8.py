def busca_binaria_palavras(lista_palavras, palavra_alvo):
    esquer, direita = 0, len(lista_palavras) - 1
    while esquer <= direita:
        meio = (esquer + direita) // 2
        if lista_palavras[meio] == palavra_alvo:
            return meio
        elif lista_palavras[meio] < palavra_alvo:
            esquer = meio + 1
        else:
            direita = meio - 1
    return -1
