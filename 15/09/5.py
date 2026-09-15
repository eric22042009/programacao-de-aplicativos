vetor = [5, 8, 3, 5, 7, 5, 10, 2, 5, 9]

numero = int(input("Digite o número que deseja buscar: "))

primeira = -1
ultima = -1

for i in range(len(vetor)):
    if vetor[i] == numero:
        if primeira == -1:
            primeira = i

        ultima = i

print("Primeira posição:", primeira)
print("Última posição:", ultima)
