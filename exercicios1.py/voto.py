def voto_corrigido(votos):
    if votos >= 15:
        return "voto aprovado"
    elif votos >= 10:
        return "ok"
    elif votos <= 5:
        return "voto recusado"
    return "sla"


assert voto_corrigido(16) == "voto aprovado"  
assert voto_corrigido(12) == "ok"             
assert voto_corrigido(7) == "sla"             
assert voto_corrigido(3) == "voto recusado"   

print("todos os testes passaram")
