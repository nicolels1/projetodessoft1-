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
      
def remover_dado(lista_rolados, lista_guardados, ind):
    lista_rolados2 = []
    lista_guardados2 = []

    lista_rolados2 = lista_rolados
    lista_rolados2.append(lista_guardados[ind])
    del lista_guardados[ind]
    lista_guardados2 = lista_guardados

    resultado = [lista_rolados2, lista_guardados2]
    return resultado

def calcula_pontos_regra_simples(lista_dados):
    soma = {}
    for i in range(1, 7):
        soma[i] = 0
        
    for face in lista_dados:
        if  soma[face] == 0:
             soma[face] = face 
        else: 
            soma[face] += face 
    return soma




        


