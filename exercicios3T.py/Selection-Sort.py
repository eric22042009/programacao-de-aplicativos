idades = [17, 11, 15, 13, 12]

for i in range(len(idades)):
    menor = i

    for j in range(i + 1, len(idades)):
        if idades[j] < idades[menor]:
            menor = j

    idades[i], idades[menor] = idades[menor], idades[i]

print("Lista final ordenada:")
print(idades)
