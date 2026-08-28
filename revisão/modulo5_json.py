import json

nome_dig = input("Digite o nome: ")
idade_dig = input("Digite a idade: ")
curso_dig = input("Digite o curso: ")

aluno = {"nome": nome_dig, "idade": idade_dig, "curso": curso_dig}

arquivo = open("aluno.json", "w")
json.dump(aluno, arquivo)
arquivo.close()

arquivo = open("aluno.json", "r")
aluno = json.load(arquivo)
arquivo.close()

print("O aluno", aluno["nome"], "está matriculado no curso", aluno["curso"])
