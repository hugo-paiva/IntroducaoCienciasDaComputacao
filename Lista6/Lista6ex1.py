quant_itens = int(input())
lista = list(range(quant_itens))
for i in range(quant_itens - 1, -1, -1): lista[i] = input()
for i, item in enumerate(lista):
    print(item, end='')
    if i != quant_itens - 1: print(end=', ')
