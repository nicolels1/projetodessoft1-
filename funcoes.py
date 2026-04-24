def rolar_dados(n):
    import random
    resultados = []
    for i in range(n):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados   
