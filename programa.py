from funcoes import *

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

imprime_cartela(cartela)
count = 0

while count < 12:
    lista_rolados = rolar_dados(5)
    lista_guardados = []
    rerrolagem = 0 
    
    while True:
        print(f'Dados rolados: {lista_rolados}')
        print(f'Dados guardados: {lista_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        while True: 
            acao = input()
            if acao not in ('0','1','2','3','4'):
                print("Opção inválida. Tente novamente.")
                continue 
            break

        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            ind = int(input())
            if ind < len(lista_rolados):
                lista_rolados, lista_guardados = guardar_dado(lista_rolados, lista_guardados, ind)

        elif acao == "2": 
            print("Digite o índice do dado a ser removido (0 a 4):")
            ind_remov = int(input())
            if ind_remov < len(lista_guardados):
                lista_rolados, lista_guardados = remover_dado(lista_rolados, lista_guardados, ind_remov)

        elif acao == "3":
            if rerrolagem == 2:
                print("Você já usou todas as rerrolagens.")
                continue
            else:
                rerrolagem += 1
                lista_rolados = rolar_dados(5-len(lista_guardados))
                continue 
                
        elif acao == "4":
            imprime_cartela(cartela)
            continue 

        else:
            unir = lista_guardados + lista_rolados
            print("Digite a combinação desejada:")

            while True:
                combinacao = input()

                lista_combinacoes = [
                    "cinco_iguais", "full_house", "quadra", "sem_combinacao",
                    "sequencia_alta", "sequencia_baixa",
                    "1", "2", "3", "4", "5", "6"
                ]

                if combinacao not in lista_combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    continue 

                elif combinacao in ["1","2","3","4","5","6"]:
                    if cartela["regra_simples"][int(combinacao)] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue 
                    else:
                        cartela = faz_jogada(unir, combinacao, cartela)
                        break

                elif combinacao in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue 
                    else:
                        cartela = faz_jogada(unir, combinacao, cartela)
                        break
            
            count += 1
            break 

soma = 0
veri_bonus = 0

for regra, pontos in cartela.items():
    for numero in pontos.values():
        if numero != -1:
            soma += numero
            if regra == "regra_simples":
                veri_bonus += numero

if veri_bonus >= 63:
    soma += 35

imprime_cartela(cartela)
print(f"Pontuação total: {soma}")