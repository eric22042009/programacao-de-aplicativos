lista = [5, 8, 5, 3, 7, 5, 10, 5, 2, 9]

valor = int(input("Digite o valor que deseja buscar: "))

contador = 0

for i in range(10):
    if lista[i] == valor:
        contador += 1

print("O valor aparece", contador, "vezes na lista.")
