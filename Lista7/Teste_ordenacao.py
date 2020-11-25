def insertionSort(lista):
    for i in range(1, len(lista)):
        daVez = lista[i]
        k = i
        while k > 0 and daVez < lista[k-1]:
            lista[k] = lista[k - 1]
            k = k - 1
            lista[k] = daVez
    return lista

print(insertionSort(input().split()))
