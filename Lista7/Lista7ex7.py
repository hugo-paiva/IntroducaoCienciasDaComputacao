num_marmitas = int(input())

sacola_termica = {}
for _ in range(num_marmitas):
    nome, *comida = input().split()
    sacola_termica[nome.lower()] = ' '.join(comida)

print(len(sacola_termica))
pedidos_ordenados = sorted(sacola_termica.items())
for pedido in pedidos_ordenados:
    print(pedido[1])
