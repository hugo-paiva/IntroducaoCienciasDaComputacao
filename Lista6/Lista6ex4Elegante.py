quant_brinq = int(input())
lista_brinq_atual = input().split()
lista_brinq_original = lista_brinq_atual[:]
contador = 0

for _ in range(5):
    brinquedo, direcao, espacos_movidos = input().split()
    espacos_movidos = int(espacos_movidos)
    if direcao == 'E':
        espacos_movidos = -espacos_movidos
    
    posi_atual = lista_brinq_atual.index(brinquedo)
    del lista_brinq_atual[posi_atual]
    posi_atual += espacos_movidos
    lista_brinq_atual.insert(posi_atual,brinquedo)
                
for index, item in enumerate(lista_brinq_atual):
    if item != lista_brinq_original[index]:
        contador += 1
print(contador)
