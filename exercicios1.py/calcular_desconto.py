def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100.0, 0) == 100.0     
assert calcular_desconto(100.0, 10) == 90.0     
assert calcular_desconto(100.0, 50) == 50.0   
assert calcular_desconto(100.0, 100) == 0.0     
assert calcular_desconto(49.99, 10) == 44.991

print("todos os teste passaram")
