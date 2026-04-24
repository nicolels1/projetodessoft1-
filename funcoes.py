def rolar_dados(n):
    import random
    resultados = []
    for i in range(n):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados   

def guardar_dado(lista_rolados, lista_guardados, ind):
    lista_rolados2 = []
    lista_guardados2 = []

    lista_guardados2 = lista_guardados
    lista_guardados2.append(lista_rolados[ind])
    del lista_rolados[ind]
    lista_rolados2 = lista_rolados
    resultado = [lista_rolados2, lista_guardados2]
    return resultado
      




