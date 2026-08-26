def dobrar(numero):
    return numero * 2

assert dobrar(3) == 6      
assert dobrar(0) == 1    # F (falha) = da erro pq dobar zero dá zero, o o sistema esperava 1
assert dobrar(-2) == -4    

print("todos os testes passaram")