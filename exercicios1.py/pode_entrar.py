def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False


assert pode_entrar(20, False) is True   
assert pode_entrar(15, True) is True    
assert pode_entrar(15, False) is False  
assert pode_entrar(18, False) is True    
assert pode_entrar(17, True) is True    

print("todos os testes passaram")