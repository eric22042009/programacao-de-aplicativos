recado = input("digite um recado: ")

arquivo = open("avisos.txt", "a")

arquivo.write(recado + "\n")

arquivo.close()

print("Recado salvo!")
