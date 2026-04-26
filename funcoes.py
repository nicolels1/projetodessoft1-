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

def calcula_pontos_soma(dados):
    soma = 0
    
    for face in dados:
        soma += face

    return soma

def  calcula_pontos_sequencia_baixa(dados): 
    sequencia_baixa = False 
    if len(dados) >= 4:
        sequencia = []
        copia_dados = []
        for num in dados:
            copia_dados.append(num)

        while len(copia_dados) != 0:
            menor_num = 10000
            for num in copia_dados:
                if num <= menor_num:
                    menor_num = num
            
            if menor_num not in sequencia:
                sequencia.append(menor_num)

            copia_dados.remove(menor_num)

        for i in range(len(sequencia) - 3):
            if sequencia[i + 1] == sequencia[i] + 1 and sequencia[i + 2] == sequencia[i] + 2 and sequencia[i + 3] == sequencia[i] + 3:
                sequencia_baixa = True
                break

    if sequencia_baixa:
        return 15 
    else:
        return 0
    
def  calcula_pontos_sequencia_alta(dados): 
    sequencia_alta = False 
    if len(dados) >= 4:
        sequencia = []
        copia_dados = []
        for num in dados:
            copia_dados.append(num)

        while len(copia_dados) != 0:
            menor_num = 10000
            for num in copia_dados:
                if num <= menor_num:
                    menor_num = num
            
            if menor_num not in sequencia:
                sequencia.append(menor_num)
                
            copia_dados.remove(menor_num)

        for i in range(len(sequencia) - 4):
            if sequencia[i + 1] == sequencia[i] + 1 and sequencia[i + 2] == sequencia[i] + 2 and sequencia[i + 3] == sequencia[i] + 3 and sequencia[i + 4] == sequencia[i] + 4:
                sequencia_alta = True
                break

    if sequencia_alta:
        return 30
    else:
        return 0
        
def calcula_pontos_full_house(dados):

    a_quant = 0
    b_quant = 0 
    teste = 0
    soma = 0
    a = dados[0]
    i = 0
    while i < len(dados):
        if dados[i] == a:
            a_quant += 1 

        if dados[i] != a and teste == 0 :
            b = dados[i]
            j = 1
            while j < len(dados):
                if dados[j] == b:
                    b_quant += 1 
                j += 1 
            teste = 1 
        
        i +=1 

    if (a_quant == 2 and b_quant == 3) or (a_quant == 3 and b_quant == 2):
        for face in dados:
            soma += face 
        return soma 
    else:
        return soma 

def calcula_pontos_quadra(dados):
    soma = 0 
    contagem = 0 
    if len(dados) < 4:
        return 0
    
    quant = {}
    for i in range(1, 7):
        quant[i] = 0

    
    for face in dados:
        quant[face] +=1 
        if quant[face] == 4:
            for face in dados:
                soma += face 
            return soma 
        
    return soma

    



