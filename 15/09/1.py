vetor = [5, 8, 12, 3, 7, 10, 15, 2, 9, 6]

numero = int(input("Digite o número que deseja buscar: "))

indice = -1

for i in range(10):
    if vetor[i] == numero:
        indice = i
        break

print("Índice:", indice)
