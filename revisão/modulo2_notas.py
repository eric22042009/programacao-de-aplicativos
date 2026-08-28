nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
faltas = int(input("digite o número de faltas: "))

media = (nota1 + nota2) / 2

if faltas > 15:
    print("Reprovado por Faltas")
elif media >= 7.0:
    print("Aprovado com Sucesso")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado por Nota")
