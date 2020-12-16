dicio = {}

destino = input().upper()
while destino.lower() != 'final':

    if destino not in dicio.keys():
        dicio[destino] = 1
    else:
        dicio[destino] += 1
    destino = input().upper()

destinos_populares = []
for key, valor in dicio.items():
    if valor == max(dicio.values()):
        destinos_populares.append(key)
ordenado = sorted(destinos_populares)

for d in ordenado:
    print(d)
