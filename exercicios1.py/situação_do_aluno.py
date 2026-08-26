def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"


assert situacao_aluno(7.5) == "Aprovado"     
assert situacao_aluno(6.0) == "Aprovado"       
assert situacao_aluno(4.0) == "Recuperação"   
assert situacao_aluno(3.0) == "Reprovado"       
assert situacao_aluno(5.9) == "Recuperação"    

print("todos os testes passaram")