import json

nome_dig = input("Digite o nome: ")
idade_dig = input("Digite a idade: ")
curso_dig = input("Digite o curso: ")

aluno = {"nome": nome_dig, "idade": idade_dig, "curso": curso_dig}

arquivo = open("aluno.json", "w")
json.dump(aluno, arquivo)                 #ABRE ou cria um arquivo chanado "aluno.jaon" no modo sscrita "w"
arquivo.close()

arquivo = open("aluno.json", "r")           #abre o mesmo arquivo mas em formato de leitura "r"
aluno = json.load(arquivo)                    #json.lead lÊ o conteudo e volta para a variavel "aluno"
arquivo.close()

print("O aluno", aluno["nome"], "está matriculado no curso", aluno["curso"])
