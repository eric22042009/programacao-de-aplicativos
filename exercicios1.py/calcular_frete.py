def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20


assert calcular_frete(80.0) == 20     
assert calcular_frete(100.0) == 10    
assert calcular_frete(150.0) == 10    
assert calcular_frete(200.0) == 0     
assert calcular_frete(250.0) == 0  


print("todos os testes passaram")
