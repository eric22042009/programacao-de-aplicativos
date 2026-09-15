vetor = [12, 5, 28, 7, 19, 3, 25, 10, 8, 15]

maior = vetor[0]
posicao = 0

for i in range(1, len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print("Maior número:", maior)
print("Posição:", posicao)