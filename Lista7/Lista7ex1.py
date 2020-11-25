def insertionSort(lista):
    for i in range(1, len(lista)):
        daVez = lista[i]
        k = i
        while k > 0 and int(daVez['dificuldade']) > int(lista[k-1]['dificuldade']):
            lista[k] = lista[k - 1]
            k = k - 1
            lista[k] = daVez
    return lista
    
    
num_problemas = int(input())
solucoes = []
problema = {}
for _ in range(num_problemas):
    problema['nome'], problema['solucao'], problema['dificuldade'] = input().split()
    solucoes.append(problema.copy())
    insertionSort(solucoes)

for s in solucoes:
    print(s['solucao'], end='')