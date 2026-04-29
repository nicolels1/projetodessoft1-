from funcoes import *
n = 5
lista_rolados = rolar_dados(n)
lista_guardados = []
rolagem = 0
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

print("Cartela de Pontos:")
imprime_cartela(cartela)
print(f'Dados rolados: {lista_rolados}')
print(f'Dados guardados: {lista_guardados}')
for i in range(12):
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = input("")
    if acao == "1":
        print("Digite o índice do dado a ser guardado (0 a 4):")
        ind = input("")
        lista_lenrolados = []
        for i in range(len(lista_rolados)):
            lista_lenrolados.append("i")

        while ind not in lista_lenrolados:
            print("Índice inválido.")
            print("Digite o índice do dado a ser guardado (0 a 4):")
            ind = input("")
        ind = int(ind)

        lista = guardar_dado(lista_rolados, lista_guardados, ind)
        lista_guardados = lista[1]
        lista_rolados = lista[0]
    elif acao == "2":
        print("Digite o índice do dado a ser removido (0 a 4):")
        ind = input("")
        lista_lenguardados = []
        for i in range(len(lista_guardados)):
            lista_lenguardados.append("i")

        while ind not in lista_lenguardados:
            print("Índice inválido.")
            print("Digite o índice do dado a ser guardado (0 a 4):")
            ind = input("")
        ind = int(ind)

        lista = remover_dado(lista_rolados, lista_guardados, ind)
        lista_guardados = lista[1]
        lista_rolados = lista[0]
    elif acao == "3":
        if rolagem >= 2:
            print("Você já usou todas as rerrolagens.")
        else:
            n = len(lista_rolados)
            lista_rolados = rolar_dados(n)
        rolagem += 1
    elif acao == "4":
        print("Cartela de Pontos:")
        imprime_cartela(cartela)
    elif acao == "0":
        print("Digite a combinação desejada:")
        combinacao = input("")
        lista_combinacoes = ["cinco_iguais", "full_house", "quadra", "sem_combinacao", "sequencia_alta", "sequencia_baixa", "1", "2", "3", "4", "5", "6"]
        if combinacao not in lista_combinacoes:
            print("Combinação inválida. Tente novamente.")
            print("Digite a combinação desejada:")
            combinacao = input("")
        if combinacao in ["1","2","3","4","5","6"]:
            if cartela["regra_simples"][int(combinacao)] != -1:
                print("Essa combinação já foi utilizada.")
        elif combinacao in cartela["regra_avancada"]:
            if cartela["regra_avancada"][combinacao] != -1:
                print("Essa combinação já foi utilizada.")
        else:
            cartela = faz_jogada(lista_guardados, combinacao, cartela)
        
    else:
        print("Opção inválida. Tente novamente.")
    print(f'Dados rolados: {lista_rolados}')
    print(f'Dados guardados: {lista_guardados}')
    

#pontuacao final
soma = 0
veri_bonus = 0
for regra, pontos in cartela.items():
    for numero in pontos.values():
        if numero != -1:
            soma += numero
            if regra == "regra_simples":
                veri_bonus += numero
#bonus
if veri_bonus >= 63:
    soma += 35

print("Cartela de Pontos:")
imprime_cartela(cartela)
print(f"Pontuação total: {soma}")



        

        
