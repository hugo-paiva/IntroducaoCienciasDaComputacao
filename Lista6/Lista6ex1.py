quant_itens = int(input())
lista = list(range(quant_itens))
for i in range(quant_itens - 1, -1, -1):
    item = input()
    lista[i] = item
for item in lista:
    print(item, end='')
    if item != lista[-1]:
        print(end=', ')
