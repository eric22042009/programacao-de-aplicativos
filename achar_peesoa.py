print("-- cdastrar pessoa --")


nome = input("nome?: ")
idade = int(input("qual sua idade?: "))
profissão = input("diga sua profissão?: ")


print(nome)
print(idade)
print(profissão)

if idade < 17:
    print("cadastro recusado") 
else: 
    print("cadastro aprovado")