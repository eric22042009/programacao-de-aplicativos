
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100.0, 10) == 90.0
assert calcular_desconto(200.0, 25) == 150.0
assert calcular_desconto(50.0, 50) == 25.0

print("todos os testes passaram")