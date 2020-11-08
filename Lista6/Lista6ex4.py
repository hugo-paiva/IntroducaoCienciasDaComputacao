quant_brinq = int(input())
lista_brinq_atual = input().split()
lista_brinq_original = lista_brinq_atual[:]
contador = 0

for _ in range(5):
    brinquedo, direcao, spaces_movidos = input().split()
    brinquedo, direcao, spaces_movidos = str(brinquedo), str(direcao), int(spaces_movidos)
    for index, item in enumerate(lista_brinq_atual):
        if item == brinquedo:
            if direcao == 'D':
                # lista_brinq_atual[index+spaces_movidos+1:index+spaces_movidos+1] = brinquedo
                # é outra maneira válida de se escrever
                lista_brinq_atual.insert(index + spaces_movidos + 1, brinquedo)
                del lista_brinq_atual[index]
                break
            else:
                lista_brinq_atual.insert(index - spaces_movidos,brinquedo)
                del lista_brinq_atual[index + 1]
                break
for index, item in enumerate(lista_brinq_atual):
    if item != lista_brinq_original[index]:
        contador += 1
print(contador)