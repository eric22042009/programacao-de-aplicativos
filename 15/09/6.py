def busca_sequencial_limites(vetor, alvo):
    primeira = -1
    ultima = -1
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            if primeira == -1:
                primeira = i
            ultima = i
    return primeira, ultima
